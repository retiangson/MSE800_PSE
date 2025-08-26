Great question! Let’s go step by step. I’ll explain **quantum gates**, their **descriptions**, and then show **sample calculations** both for **single-qubit** and **multi-qubit** cases.

---

# 🔹 1. Basics

* In quantum computing, a **qubit** is represented as a vector in a **2D complex space**:

  $$
  |0\rangle = \begin{bmatrix}1 \\ 0\end{bmatrix}, \quad |1\rangle = \begin{bmatrix}0 \\ 1\end{bmatrix}
  $$
* A general qubit state:

  $$
  |\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \quad \text{where } |\alpha|^2 + |\beta|^2 = 1
  $$
* Gates are **unitary matrices** (they preserve probability).
* Applying a gate = multiplying the gate matrix with the qubit vector.

---

# 🔹 2. Single-Qubit Gates

### **Identity (I)**

Does nothing.

$$
I = \begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix}
$$

Example:

$$
I|0\rangle = |0\rangle
$$

---

### **Pauli-X (NOT gate)**

Flips $|0\rangle \leftrightarrow |1\rangle$.

$$
X = \begin{bmatrix}0 & 1 \\ 1 & 0\end{bmatrix}
$$

Example:

$$
X|0\rangle = \begin{bmatrix}0 & 1 \\ 1 & 0\end{bmatrix}\begin{bmatrix}1 \\ 0\end{bmatrix} = \begin{bmatrix}0 \\ 1\end{bmatrix} = |1\rangle
$$

---

### **Pauli-Y**

Combines bit flip and phase.

$$
Y = \begin{bmatrix}0 & -i \\ i & 0\end{bmatrix}
$$

Example:

$$
Y|0\rangle = i|1\rangle
$$

---

### **Pauli-Z (Phase flip)**

Leaves $|0\rangle$, flips sign of $|1\rangle$.

$$
Z = \begin{bmatrix}1 & 0 \\ 0 & -1\end{bmatrix}
$$

Example:

$$
Z|1\rangle = -|1\rangle
$$

---

### **Hadamard (H)**

Creates superposition.

$$
H = \frac{1}{\sqrt{2}}\begin{bmatrix}1 & 1 \\ 1 & -1\end{bmatrix}
$$

Examples:

$$
H|0\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle + |1\rangle), \quad H|1\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle - |1\rangle)
$$

---

### **Phase (S and T)**

* **S gate** (π/2 phase):

$$
S = \begin{bmatrix}1 & 0 \\ 0 & i\end{bmatrix}
$$

$$
S|1\rangle = i|1\rangle
$$

* **T gate** (π/4 phase):

$$
T = \begin{bmatrix}1 & 0 \\ 0 & e^{i\pi/4}\end{bmatrix}
$$

---

### **Rotation Gates**

* Rotate around an axis of the Bloch sphere.

$$
R_x(\theta) = e^{-i\theta X/2}, \quad R_y(\theta), \quad R_z(\theta)
$$

Example:

$$
R_z(\pi)|1\rangle = -|1\rangle
$$

---

# 🔹 3. Multi-Qubit Gates

For **n qubits**, the state vector has size $2^n$. Gates act using **tensor products**.

---

### **CNOT (Controlled-NOT)**

If **control qubit = 1**, flip the target.
Matrix (for 2 qubits):

$$
CNOT = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}
$$

Example: Apply to $|10\rangle$:

$$
CNOT|10\rangle = |11\rangle
$$

---

### **Controlled-Z**

Flips the phase if both are $|1\rangle$.

$$
CZ = \text{diag}(1,1,1,-1)
$$

---

### **SWAP**

Swaps two qubits.

$$
SWAP|01\rangle = |10\rangle
$$

---

### **Toffoli (CCNOT)**

3-qubit gate: if **two controls = 1**, flip target.

---

# 🔹 4. Example Calculations

✅ **Single Qubit**:
Start in $|0\rangle$. Apply Hadamard:

$$
H|0\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle + |1\rangle)
$$

This means **50% chance of measuring 0, 50% chance of measuring 1**.

---

✅ **Two Qubits (Entanglement)**:
Start in $|00\rangle$. Apply Hadamard on first qubit, then CNOT:

$$
H|0\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle+|1\rangle)
$$

So state =

$$
\tfrac{1}{\sqrt{2}}(|00\rangle + |10\rangle)
$$

Then apply CNOT:

$$
\tfrac{1}{\sqrt{2}}(|00\rangle + |11\rangle)
$$

This is a **Bell state** (maximally entangled). Measuring one qubit instantly tells you the other.

---

# 🔹 5. Summary

* **Single-qubit gates**: I, X, Y, Z, H, S, T, rotations.
* **Multi-qubit gates**: CNOT, CZ, SWAP, Toffoli.
* **Calculation = Matrix × State vector**.
* Used to build **superposition** and **entanglement**.

---

Would you like me to also **draw the quantum circuits step-by-step** for these examples (Hadamard + CNOT entanglement, etc.) so you can visualize how the gates connect?
