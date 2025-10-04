## Quantum Gates

Quantum gates are the building blocks of quantum circuits, analogous to logic gates in classical computing. Unlike classical gates, which operate irreversibly on bits, quantum gates are represented by **unitary matrices**, making them reversible and capable of manipulating qubits in **superposition** and **entanglement** (Nielsen & Chuang, 2010). On the Bloch sphere, gates correspond to rotations around specific axes (Bloch_sphere.pdf).

---

### 1. Single-Qubit Gates

- **Identity (I)** – Leaves the qubit unchanged  
  \[
  I = \begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix}
  \]

- **Pauli-X (NOT Gate)** – Flips \(|0⟩ \leftrightarrow |1⟩\)  
  \[
  X = \begin{bmatrix}0 & 1 \\ 1 & 0\end{bmatrix}
  \]

- **Pauli-Y** – Rotation around the y-axis, adds a phase factor  
  \[
  Y = \begin{bmatrix}0 & -i \\ i & 0\end{bmatrix}
  \]

- **Pauli-Z** – Phase flip; leaves \(|0⟩\) unchanged, flips the phase of \(|1⟩\)  
  \[
  Z = \begin{bmatrix}1 & 0 \\ 0 & -1\end{bmatrix}
  \]

- **Hadamard (H)** – Creates superposition from a basis state  
  \[
  H = \tfrac{1}{\sqrt{2}} \begin{bmatrix}1 & 1 \\ 1 & -1\end{bmatrix}
  \]  
  Example: \( H|0⟩ = (|0⟩ + |1⟩)/\sqrt{2} \)

- **Phase Gate (S)** – Adds a phase of \(i\) to \(|1⟩\)  
  \[
  S = \begin{bmatrix}1 & 0 \\ 0 & i\end{bmatrix}
  \]

- **π/8 Gate (T)** – Adds a smaller phase of \(e^{i\pi/4}\) to \(|1⟩\), important for universality  
  \[
  T = \begin{bmatrix}1 & 0 \\ 0 & e^{i\pi/4}\end{bmatrix}
  \]

---

### 2. Multi-Qubit Gates

- **Controlled-NOT (CNOT)** – Flips target qubit if control qubit is \(|1⟩\)  
  \[
  CNOT =
  \begin{bmatrix}
  1 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 \\
  0 & 0 & 0 & 1 \\
  0 & 0 & 1 & 0
  \end{bmatrix}
  \]

- **SWAP Gate** – Exchanges the states of two qubits  
  \[
  SWAP =
  \begin{bmatrix}
  1 & 0 & 0 & 0 \\
  0 & 0 & 1 & 0 \\
  0 & 1 & 0 & 0 \\
  0 & 0 & 0 & 1
  \end{bmatrix}
  \]

- **Toffoli (CCNOT)** – A 3-qubit gate that flips the target only if *both* controls are \(|1⟩\).  
- **Fredkin (Controlled-SWAP)** – Swaps two targets if the control qubit is \(|1⟩\).  

---

### 3. Universal Gate Sets

A small set of gates can approximate any quantum computation. One widely used universal set is:  

\[
\{ H, T, CNOT \}
\]

This demonstrates that quantum computation does not require infinitely many gates, only a carefully chosen finite set (Nielsen & Chuang, 2010).

---

### Why Quantum Gates Matter

Quantum gates differ fundamentally from classical gates in three ways:

1. **Reversibility** – All operations can be undone, preserving information.  
2. **Superposition Control** – Gates rotate qubits on the Bloch sphere.  
3. **Entanglement Generation** – Multi-qubit gates like CNOT create correlations that classical systems cannot replicate.  

---

### References

- Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*. Cambridge University Press.  
- Bloch Sphere notes. *Bloch_sphere.pdf*. Yoobee College.
