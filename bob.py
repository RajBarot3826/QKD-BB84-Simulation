import random

class Bob:
    def __init__(self, n_bits):
        self.n_bits = n_bits
        self.bases = [random.choice(['Z', 'X']) for _ in range(n_bits)]

    def measure(self, alice_bits, alice_bases):
        measured_bits = []

        for i in range(self.n_bits):
            if self.bases[i] == alice_bases[i]:
                measured_bits.append(alice_bits[i])
            else:
                measured_bits.append(random.randint(0, 1))

        return measured_bits
