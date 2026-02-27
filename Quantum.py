from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Add a Hadamard gate to qubit 0
qc.h(0)

# Add a CNOT gate on control qubit 0 and target qubit 1
qc.cx(0, 1)

# Map the quantum measurement to the classical bits
qc.measure([0, 1], [0, 1])

# Use AerSimulator
simulator = AerSimulator()

# Compile the circuit for the simulator
compiled_circuit = transpile(qc, simulator)

# Run the job
job = simulator.run(compiled_circuit, shots=1000)

# Grab results from the job
result = job.result()

# Return counts
counts = result.get_counts(compiled_circuit)
print(f"\nTotal counts for {{'00', '11'}}: {counts}")