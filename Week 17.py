import numpy as np
from qiskit import QuantumCircuit, execute, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
from qiskit.quantum_info import random_unitary
print('Libraries imported successfully!')

qc = QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
qc.draw()

qc.z(0)
qc.x(0)
qc.draw()

qc.z(0)
qc.x(0)
qc.draw()

qc.measure([0,1],[0,1])
qc.draw()

