import qiskit

from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram

n = 4
n_q = n
n_b = n
qc_output = QuantumCircuit(n_q, n_b)

for j in range(n):
    qc_output.measure(j, j)

qc_output.draw()

sim = Aer.get_backend('qasm_simulator')  # this is the simulator we'll use
qobj = assemble(qc_output)  # this turns the circuit into an object our backend can run
result = sim.run(qobj).result()  # we run the experiment and get the result from that experiment
# from the results, we get a dictionary containing the number of times (counts)
# each result appeared
counts = result.get_counts()

print(counts)
# and display it on a histogram
plot_histogram(counts)

qc_encode = QuantumCircuit(n)
#qc_encode.x(7)
qc_encode.draw()