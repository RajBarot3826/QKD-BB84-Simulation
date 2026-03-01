import random

class Alice:
    def __init__(self, n_bits):
        self.n_bits = n_bits
        self.bits = [random.randint(0, 1) for _ in range(n_bits)]
        self.bases = [random.choice(['Z', 'X']) for _ in range(n_bits)]

    def send_qubits(self):
        return self.bits, self.bases
