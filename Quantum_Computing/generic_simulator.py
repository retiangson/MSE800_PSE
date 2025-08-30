import numpy as np

# === Define Basic Gates as Matrices ===

# Pauli-X (NOT gate)
X = np.array([[0, 1],
              [1, 0]])

# Pauli-Z
Z = np.array([[1,  0],
              [0, -1]])

# Hadamard Gate
H = (1/np.sqrt(2)) * np.array([[1,  1],
                               [1, -1]])

# Identity Gate
I = np.eye(2)

# CNOT (Controlled-X) for two qubits: control=0, target=1
CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]])

# === Helper: Tensor product for multi-qubit gates ===
def tensor(*ops):
    """Compute tensor product of a sequence of matrices."""
    result = ops[0]
    for op in ops[1:]:
        result = np.kron(result, op)
    return result

# === Initial state: |00> ===
zero_state = np.array([1, 0])
initial_state = np.kron(zero_state, zero_state)  # |0> ⊗ |0> = [1,0,0,0]

# === Map gate names to matrices ===
single_qubit_gates = {
    'I': I,
    'X': X,
    'Z': Z,
    'H': H
}

# === Apply single-qubit gate to qubit 0 or 1 in 2-qubit system ===
def apply_single_gate(gate_matrix, target_qubit):
    """Apply a single-qubit gate to a specific qubit (0 or 1)."""
    if target_qubit == 0:
        return tensor(gate_matrix, I)  # gate on qubit 0, I on qubit 1
    elif target_qubit == 1:
        return tensor(I, gate_matrix)  # I on qubit 0, gate on qubit 1
    else:
        raise ValueError("Qubit index must be 0 or 1.")

# === Main Simulator Function ===
def simulate_circuit():
    print("🔧 Two-Qubit Quantum Circuit Simulator (Max Depth: 3)")
    print("Supported gates: I, X, Z, H (single-qubit), CNOT (two-qubit)")
    print("Gate format:")
    print("  - Single-qubit: 'gate qubit'  (e.g., 'H 0', 'X 1')")
    print("  - Two-qubit: 'CNOT c t'      (e.g., 'CNOT 0 1')")
    print("Enter up to 3 operations. Type 'run' to simulate.\n")

    operations = []
    max_depth = 3

    # Input loop
    while len(operations) < max_depth:
        user_input = input(f"[{len(operations) + 1}] Enter operation (or 'run'): ").strip()
        if user_input.lower() == 'run':
            break
        if not user_input:
            continue
        operations.append(user_input)

    if len(operations) > max_depth:
        print("❌ Circuit exceeds maximum depth of 3.")
        return

    # Start with identity evolution
    total_unitary = np.eye(4, dtype=complex)  # 4x4 for two qubits

    # Process each operation
    for op_str in operations:
        parts = op_str.split()
        try:
            if parts[0] == 'CNOT':
                if len(parts) != 3:
                    raise ValueError("CNOT requires two qubit indices: 'CNOT c t'")
                c, t = int(parts[1]), int(parts[2])
                if c not in [0,1] or t not in [0,1] or c == t:
                    raise ValueError("CNOT control and target must be 0 or 1 and different.")
                # We only support CNOT(0,1) directly. For CNOT(1,0), build it.
                if c == 0 and t == 1:
                    gate_matrix = CNOT
                elif c == 1 and t == 0:
                    # CNOT with qubit 1 as control, qubit 0 as target
                    cx_10 = tensor(H, H) @ CNOT @ tensor(H, H)  # Not standard, better to build directly
                    # Actually, use swap or define manually
                    # Simpler: Use known matrix for CNOT(1,0)
                    gate_matrix = np.array([[1,0,0,0],
                                            [0,0,0,1],
                                            [0,0,1,0],
                                            [0,1,0,0]])
                else:
                    raise ValueError("Unsupported CNOT configuration.")
            elif parts[0] in single_qubit_gates:
                if len(parts) != 2:
                    raise ValueError("Single-qubit gate: 'gate qubit'")
                gate_name, qubit_idx = parts[0], int(parts[1])
                if qubit_idx not in [0,1]:
                    raise ValueError("Qubit index must be 0 or 1.")
                gate_matrix = apply_single_gate(single_qubit_gates[gate_name], qubit_idx)
            else:
                raise ValueError(f"Unknown gate: {parts[0]}")

            # Apply gate: total_unitary = current_gate @ total_unitary
            total_unitary = gate_matrix @ total_unitary

        except Exception as e:
            print(f"❌ Error in operation '{op_str}': {e}")
            return

    # Compute final state
    final_state = total_unitary @ initial_state

    # Output
    print("\n✅ Simulation Complete")
    print("Initial state |00>:", initial_state)
    print("Final state:      ", np.round(final_state, 5))
    print("Probabilities:    ", np.round(np.abs(final_state)**2, 5))
    print("State vector shape:", final_state.shape)

    # Optional: Show which basis states
    basis = ['|00>', '|01>', '|10>', '|11>']
    print("\nFinal State Breakdown:")
    for i, amp in enumerate(final_state):
        prob = abs(amp)**2
        if prob > 1e-6:
            phase = np.angle(amp)
            print(f"{basis[i]}: {amp:.4f} (prob: {prob:.4f}, phase: {phase:.2f} rad)")

# === Run the simulator ===
if __name__ == "__main__":
    simulate_circuit()