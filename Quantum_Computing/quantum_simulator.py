#!/usr/bin/env python3
"""quantum_simulator.py
Multi-qubit state-vector simulator with a single-line diagram input feature.

Usage examples:
  python3 quantum_simulator.py "|0>->H->X->MEASURE(10)"
  python3 quantum_simulator.py --diagram "|00>→H(0)→CNOT(0,1)→MEASURE(100)"
  python3 quantum_simulator.py            # interactive prompt
  python3 quantum_simulator.py --init "|00>" --gates "H(0) CNOT(0,1)"
"""

from __future__ import annotations
import numpy as np, math, cmath, re, sys, argparse, random
from math import sqrt, isclose

# --- Basic single-qubit states ---
ket0 = np.array([1,0], dtype=complex)
ket1 = np.array([0,1], dtype=complex)
ket_plus = (ket0 + ket1) / sqrt(2)
ket_minus = (ket0 - ket1) / sqrt(2)

# --- Single-qubit gate matrices ---
I2 = np.eye(2, dtype=complex)
X = np.array([[0,1],[1,0]], dtype=complex)
Y = np.array([[0,-1j],[1j,0]], dtype=complex)
Z = np.array([[1,0],[0,-1]], dtype=complex)
H = np.array([[1,1],[1,-1]], dtype=complex) / sqrt(2)
S = np.array([[1,0],[0,1j]], dtype=complex)
T = np.array([[1,0],[0,cmath.exp(1j*math.pi/4)]], dtype=complex)

_safe_math = {
    "sqrt": math.sqrt, "pi": math.pi, "e": math.e,
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "exp": cmath.exp, "I": 1j, "i": 1j, "j": 1j, "complex": complex, "abs": abs
}

def safe_eval(expr: str):
    expr = expr.strip()
    if expr == "": raise ValueError("Empty expression")
    return eval(expr, {"__builtins__": None}, _safe_math.copy())

def parse_angle(s: str) -> float:
    s = s.strip()
    if s.endswith("deg") or s.endswith("°"):
        core = s.rstrip("deg").rstrip("°")
        val = safe_eval(core)
        return float(val) * math.pi / 180.0
    return float(safe_eval(s))

# Rotation gates
def Rx(theta):
    t2 = theta/2.0
    return np.array([[math.cos(t2), -1j*math.sin(t2)],[-1j*math.sin(t2), math.cos(t2)]], dtype=complex)
def Ry(theta):
    t2 = theta/2.0
    return np.array([[math.cos(t2), -math.sin(t2)],[math.sin(t2), math.cos(t2)]], dtype=complex)
def Rz(theta):
    return np.array([[cmath.exp(-1j*theta/2.0),0],[0, cmath.exp(1j*theta/2.0)]], dtype=complex)
def Phase(theta): return np.array([[1,0],[0, cmath.exp(1j*theta)]], dtype=complex)
def U3(theta, phi, lam):
    t2 = math.cos(theta/2.0); s2 = math.sin(theta/2.0)
    return np.array([[t2, -cmath.exp(1j*lam)*s2],[cmath.exp(1j*phi)*s2, cmath.exp(1j*(phi+lam))*t2]], dtype=complex)

# --- Multi-qubit helpers ---
def kron_n(mats):
    out = np.array([1.0], dtype=complex)
    for M in mats:
        out = np.kron(out, M)
    return out

def apply_single_qubit_gate(state, gate, qubit, n_qubits):
    # qubit: 0 is most-significant (leftmost) in ket string notation |q0 q1 ...>
    mats = []
    for i in range(n_qubits):
        if i == qubit:
            mats.append(gate)
        else:
            mats.append(I2)
    U = kron_n(mats)
    return U.dot(state)

def make_controlled(gate, control, target, n_qubits):
    P0 = np.array([[1,0],[0,0]], dtype=complex)
    P1 = np.array([[0,0],[0,1]], dtype=complex)
    mats0 = [I2]*n_qubits
    mats1 = [I2]*n_qubits
    mats0[control] = P0
    mats1[control] = P1
    mats1[target] = gate
    U0 = kron_n(mats0)
    U1 = kron_n(mats1)
    return U0 + U1

def make_swap(a,b,n_qubits):
    dim = 2**n_qubits
    U = np.zeros((dim, dim), dtype=complex)
    for i in range(dim):
        bits = list(format(i, f"0{n_qubits}b"))
        jbits = bits.copy()
        jbits[a], jbits[b] = jbits[b], jbits[a]
        j = int("".join(jbits), 2)
        U[j,i] = 1.0
    return U

# --- State parsing ---
def normalize_ket_input(s: str) -> str:
    s = s.replace("∣","|").replace("⟩",">").replace("⟨","<").replace("｜","|")
    return s.strip()

def parse_ket_expression(s: str, n_qubits_hint=None):
    s = normalize_ket_input(s)
    sl = s.lower()
    if sl in ("|0>","0","|0⟩"):
        return ket0.copy(), 1
    if sl in ("|1>","1","|1⟩"):
        return ket1.copy(), 1
    if sl in ("|+>","+"):
        return ket_plus.copy(), 1
    if sl in ("|->","-"):
        return ket_minus.copy(), 1
    # check multi-qubit simple basis like |00>, |01>, etc
    m = re.fullmatch(r'\|([01]+)\>', s)
    if m:
        bits = m.group(1)
        vec = np.zeros((2**len(bits),), dtype=complex)
        idx = int(bits, 2)
        vec[idx] = 1.0
        return vec, len(bits)
    # otherwise try to eval expressions like "(1/sqrt(2))|00> + (1/sqrt(2))|11>"
    expr = s
    # find all basis kets like |00>, |01>, etc
    ket_tokens = sorted(set(re.findall(r'\|[01]+\>', expr)), key=lambda x:(-len(x),x))
    ctx = {}
    for i,kt in enumerate(ket_tokens):
        bits = kt[1:-1]
        arr = np.zeros((2**len(bits),), dtype=complex)
        arr[int(bits,2)] = 1.0
        name = f"V{i}"
        expr = expr.replace(kt, name)
        ctx[name] = arr
    # Also support single-qubit |0> and |1> by replacing with V_SINGLE_0 etc
    expr = expr.replace("|0>", "V_SINGLE_0").replace("|1>", "V_SINGLE_1")
    if "V_SINGLE_0" in expr or "V_SINGLE_1" in expr:
        # we will eval and then map these into the correct-sized space later
        ctx["V_SINGLE_0"] = ket0.copy()
        ctx["V_SINGLE_1"] = ket1.copy()
    try:
        val = eval(expr, {"__builtins__": None}, {**_safe_math, **ctx})
    except Exception as e:
        raise ValueError(f"Couldn't parse ket expression {s!r}: {e}")
    arr = np.array(val, dtype=complex)
    if arr.ndim != 1:
        raise ValueError("Parsed ket must be a vector (1-d array)")
    # If single-qubit vectors were used but the expression combined different sizes, try to promote to uniform size
    size = arr.size
    if not (size & (size-1))==0:
        raise ValueError("Parsed ket length is not power-of-two")
    return arr, int(math.log2(size))

# --- Pretty printing ---
def state_to_dirac(state, n_qubits=None, tol=1e-9):
    state = np.array(state, dtype=complex)
    if n_qubits is None:
        n_qubits = int(math.log2(state.size))
    # normalize and remove global phase
    norm = np.linalg.norm(state)
    if norm < tol: return "0"
    v = state / norm
    k = int(np.argmax(np.abs(v)))
    ph = cmath.phase(v[k]) if abs(v[k])>tol else 0.0
    v = v * cmath.exp(-1j*ph)
    # single-qubit shortcuts
    if n_qubits == 1:
        if np.allclose(v, ket0, atol=1e-8): return "|0⟩"
        if np.allclose(v, ket1, atol=1e-8): return "|1⟩"
        if np.allclose(v, ket_plus, atol=1e-8): return "|+⟩ (|0⟩+|1⟩)/√2"
        if np.allclose(v, ket_minus, atol=1e-8): return "|-⟩ (|0⟩-|1⟩)/√2"
    # list nonzero amplitudes
    parts = []
    for idx,amp in enumerate(v):
        if abs(amp) > 1e-8:
            bits = format(idx, f"0{n_qubits}b")
            a = amp
            a_str = f"{a.real:.6g}" if abs(a.imag) < 1e-10 else f"{a.real:.6g}{'+' if a.imag>=0 else ''}{a.imag:.6g}j"
            parts.append(f"({a_str})|{bits}⟩")
    return " + ".join(parts)

def measure_state(state, n_qubits, shots=1, collapse=True):
    probs = np.abs(state)**2
    if shots == 1 and collapse:
        r = random.random()
        cum = 0.0
        for idx,p in enumerate(probs):
            cum += p
            if r <= cum:
                new = np.zeros_like(state); new[idx] = 1.0
                return {format(idx, f"0{n_qubits}b"): 1}, new
    outcomes = np.random.choice(len(probs), size=shots, p=probs)
    counts = {}
    for o in outcomes:
        key = format(o, f"0{n_qubits}b")
        counts[key] = counts.get(key,0)+1
    if shots == 1 and collapse:
        idx = outcomes[0]
        new = np.zeros_like(state); new[idx] = 1.0
        return counts, new
    return counts, state.copy()

# --- Gate tokenization & building ---
_token_re = re.compile(r'([A-Za-z][A-Za-z0-9_]*)\s*(\([^)]*\))?')
def tokenize_gates(s: str):
    s2 = s.replace("->"," ").replace("→"," ")  # keep commas inside parentheses for arg lists

    parts = _token_re.findall(s2)
    tokens = []
    for name,args in parts:
        args = args[1:-1] if args else ""
        tokens.append((name.upper(), args))
    return tokens

def gate_from_token(name, args, n_qubits):
    name = name.upper()
    if name == "I": return ("SINGLE", I2, None)
    if name == "X": return ("SINGLE", X, None)
    if name == "Y": return ("SINGLE", Y, None)
    if name == "Z": return ("SINGLE", Z, None)
    if name == "H": return ("SINGLE", H, None)
    if name == "S": return ("SINGLE", S, None)
    if name == "T": return ("SINGLE", T, None)
    if name.startswith("RX"):
        th = parse_angle(args); return ("SINGLE", Rx(th), None)
    if name.startswith("RY"):
        th = parse_angle(args); return ("SINGLE", Ry(th), None)
    if name.startswith("RZ"):
        th = parse_angle(args); return ("SINGLE", Rz(th), None)
    if name in ("P","PHASE"):
        th = parse_angle(args); return ("SINGLE", Phase(th), None)
    if name in ("U","U3"):
        parts = [p.strip() for p in args.split(",")]
        if len(parts)!=3: raise ValueError("U(theta,phi,lam) requires 3 args")
        th = parse_angle(parts[0]); ph = parse_angle(parts[1]); lam = parse_angle(parts[2])
        return ("SINGLE", U3(th, ph, lam), None)
    if name in ("CNOT","CX"):
        c,t = [int(x) for x in args.split(",")]
        return ("CONTROLLED", ("CNOT", c, t), None)
    if name == "CZ":
        c,t = [int(x) for x in args.split(",")]
        return ("CONTROLLED", ("CZ", c, t), None)
    if name == "SWAP":
        a,b = [int(x) for x in args.split(",")]
        return ("GLOBAL", make_swap(a,b,n_qubits), f"SWAP({a},{b})")
    if name.startswith("CU"):
        parts = [p.strip() for p in args.split(",")]
        if len(parts) < 3: raise ValueError("CU requires at least control,target,GateName")
        c = int(parts[0]); t = int(parts[1]); gname = parts[2]
        gargs = ",".join(parts[3:]) if len(parts)>3 else ""
        gt = gate_from_token(gname, gargs, n_qubits)
        if gt[0]!="SINGLE": raise ValueError("CU only supports single-qubit target gates")
        return ("CONTROLLED", ("CU", c, t, gt[1]), None)
    if name in ("MEASURE","M","MEASUREZ"):
        shots = 1
        collapse = True
        if args:
            if "=" in args:
                kv = dict([tuple(x.split("=")) for x in args.split(",")])
                shots = int(kv.get("shots", kv.get("n", "1")))
                collapse = kv.get("collapse", "True").lower() in ("1","true","yes")
            else:
                shots = int(args)
        return ("MEASURE", shots, collapse)
    raise ValueError(f"Unknown gate token: {name}")

def build_tokens_from_text(gate_text, n_qubits, target_hint=0):
    toks = []
    pairs = tokenize_gates(gate_text)
    for name,args in pairs:
        upper = name.upper()
        # Single-qubit gates and parameterized ones
        if upper in ("I","X","Y","Z","H","S","T","P","PHASE","RX","RY","RZ","U","U3"):
            target = None
            gate_args = ""
            if args:
                # support "angle;target" or "target;angle" forms using semicolon
                if ";" in args:
                    left,right = args.split(";",1)
                    if re.fullmatch(r'\d+', left.strip()): target = int(left.strip()); gate_args = right.strip()
                    elif re.fullmatch(r'\d+', right.strip()): target = int(right.strip()); gate_args = left.strip()
                    else:
                        gate_args = args
                elif re.fullmatch(r'\d+', args.strip()):
                    target = int(args.strip())
                else:
                    gate_args = args
            # build matrix
            if upper in ("RX","RY","RZ","P","PHASE","U","U3"):
                if upper=="RX": mat = Rx(parse_angle(gate_args))
                elif upper=="RY": mat = Ry(parse_angle(gate_args))
                elif upper=="RZ": mat = Rz(parse_angle(gate_args))
                elif upper in ("P","PHASE"): mat = Phase(parse_angle(gate_args))
                else:
                    parts = [p.strip() for p in gate_args.split(",")]
                    if len(parts)!=3: raise ValueError("U requires theta,phi,lam")
                    mat = U3(parse_angle(parts[0]), parse_angle(parts[1]), parse_angle(parts[2]))
                toks.append(("SINGLE", mat, target if target is not None else target_hint))
            else:
                mat_map = {"I":I2,"X":X,"Y":Y,"Z":Z,"H":H,"S":S,"T":T}
                toks.append(("SINGLE", mat_map[upper], target if target is not None else target_hint))
        elif upper in ("CNOT","CX","CZ","SWAP") or upper.startswith("CU"):
            gtok = gate_from_token(upper, args, n_qubits)
            toks.append(gtok)
        elif upper in ("MEASURE","M","MEASUREZ"):
            mtok = gate_from_token(upper, args, n_qubits)
            toks.append(mtok)
        else:
            raise ValueError(f"Unknown gate name in build_tokens: {name}")
    return toks

# --- Runner ---
def run_circuit(initial_state, n_qubits, tokens, verbose=True):
    state = np.array(initial_state, dtype=complex)
    step = 0
    if verbose:
        print("Initial:", state_to_dirac(state, n_qubits))
    for tok in tokens:
        kind = tok[0]
        if kind == "SINGLE":
            gate = tok[1]
            target = tok[2]
            if target is None:
                raise ValueError("Single-qubit gate missing target index. Use notation like H(0) or provide a default target_hint.")
            state = apply_single_qubit_gate(state, gate, target, n_qubits)
            step += 1
            if verbose:
                print(f"Step {step}: SINGLE on q{target} -> {state_to_dirac(state,n_qubits)}")
        elif kind == "CONTROLLED":
            info = tok[1]
            if info[0] == "CNOT":
                _, c, t = info
                U = make_controlled(X, c, t, n_qubits)
                state = U.dot(state)
                step += 1
                if verbose: print(f"Step {step}: CNOT({c},{t}) -> {state_to_dirac(state,n_qubits)}")
            elif info[0] == "CZ":
                _, c, t = info
                U = make_controlled(Z, c, t, n_qubits)
                state = U.dot(state)
                step += 1
                if verbose: print(f"Step {step}: CZ({c},{t}) -> {state_to_dirac(state,n_qubits)}")
            elif info[0] == "CU":
                _, c, t, gmat = info
                U = make_controlled(gmat, c, t, n_qubits)
                state = U.dot(state)
                step += 1
                if verbose: print(f"Step {step}: CU on control {c} target {t} -> {state_to_dirac(state,n_qubits)}")
            else:
                raise ValueError("Unknown controlled type")
        elif kind == "GLOBAL":
            mat = tok[1]
            state = mat.dot(state)
            step += 1
            if verbose: print(f"Step {step}: GLOBAL -> {state_to_dirac(state,n_qubits)}")
        elif kind == "MEASURE":
            shots = tok[1]; collapse = tok[2]
            counts, newstate = measure_state(state, n_qubits, shots=shots, collapse=collapse)
            step += 1
            if verbose:
                print(f"Step {step}: MEASURE shots={shots} collapse={collapse} -> counts={counts}")
            state = newstate
        else:
            raise ValueError("Unknown op kind: "+str(kind))
    return state

def gate_name(mat):
    if np.allclose(mat, X): return "X"
    if np.allclose(mat, Y): return "Y"
    if np.allclose(mat, Z): return "Z"
    if np.allclose(mat, H): return "H"
    return "gate"

# --- New: diagram parsing and running ---
def run_diagram(diagram_str: str, default_target=0):
    # split on arrows (accept → or ->)
    parts = re.split(r'\s*(?:→|->)\s*', diagram_str.strip())
    if len(parts) == 0 or not parts[0].startswith("|"):
        raise ValueError("Diagram must start with a ket like |0>, |00>, |+>, ...")
    init_token = parts[0]
    gate_tokens = parts[1:]
    # parse initial ket
    init_vec, n_qubits = parse_ket_expression(init_token)
    # join gate tokens into a space-separated string for tokenizer
    gate_text = " ".join(gate_tokens)
    if gate_text.strip() == "":
        print("Diagram contained only initial ket. State:", state_to_dirac(init_vec, n_qubits))
        return init_vec
    tokens = build_tokens_from_text(gate_text, n_qubits, target_hint=default_target)
    # run
    final = run_circuit(init_vec, n_qubits, tokens, verbose=True)

    # compact diagram: build names for gates
    pretty_gates = []
    for tok in tokens:
        if tok[0] == "SINGLE":
            pretty_gates.append(gate_name(tok[1]) + (f"(q{tok[2]})" if tok[2] is not None else ""))
        elif tok[0] == "CONTROLLED":
            info = tok[1]
            if info[0] == "CNOT":
                pretty_gates.append(f"CNOT({info[1]},{info[2]})")
            elif info[0] == "CZ":
                pretty_gates.append(f"CZ({info[1]},{info[2]})")
            else:
                pretty_gates.append("CONTROLLED")
        elif tok[0] == "GLOBAL":
            pretty_gates.append(str(tok[2]))
        elif tok[0] == "MEASURE":
            pretty_gates.append(f"MEASURE({tok[1]})")
    print("\nCompact diagram:")
    print(f"{state_to_dirac(init_vec,n_qubits)}" + " -> " + " -> ".join(pretty_gates) + " -> " + state_to_dirac(final, n_qubits))
    return final

# --- CLI glue ---
def cli_main(argv=None):
    parser = argparse.ArgumentParser(description="Multi-qubit state-vector simulator (diagram input supported)")
    parser.add_argument("diagram", nargs="?", help="One-line diagram, e.g. '|0>->H->X->MEASURE(10)'")
    parser.add_argument("--init", "-i", help="Initial ket (legacy)", default=None)
    parser.add_argument("--gates", "-g", help="Gates text (legacy)", default=None)
    parser.add_argument("--target", "-t", type=int, default=0, help="Default target qubit for single-qubit gates when unspecified")
    parser.add_argument("--n", type=int, default=None, help="Number of qubits (optional; inferred from init)")
    args, unknown = parser.parse_known_args(argv)
    try:
        if args.diagram:
            run_diagram(args.diagram, default_target=args.target)
        elif args.init and args.gates:
            init_vec, n_qubits = parse_ket_expression(args.init)
            if args.n is not None and args.n != n_qubits:
                if args.n > n_qubits:
                    pad = np.zeros(2**args.n, dtype=complex); pad[:init_vec.size] = init_vec; init_vec = pad; n_qubits = args.n
                else:
                    raise ValueError("Specified n smaller than parsed init size")
            tokens = build_tokens_from_text(args.gates, n_qubits, target_hint=args.target)
            run_circuit(init_vec, n_qubits, tokens, verbose=True)
        else:
            # interactive prompt
            while True:
                try:
                    print("\n==========================================================")
                    diagram = input("Enter diagram (e.g. |0>->H->X->MEASURE): ").strip()
                    if diagram.strip().lower() in {"quit", "exit"}:
                        print("Goodbye!")
                        break
                    run_diagram(diagram)
                except Exception as e:
                                print(f"\n[Error] {e}")
                                print("Let's try again...\n")
                #if diagram == "":
                #    print("No diagram provided. Exiting.")
                #    return
                #run_diagram(diagram, default_target=args.target)
                
    except Exception as e:
        print("Error running diagram:", e)

if __name__ == "__main__":
    cli_main(sys.argv[1:])
