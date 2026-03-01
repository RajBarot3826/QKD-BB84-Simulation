import random

class QuantumChannel:
    def __init__(self, eve_present=False):
        self.eve_present = eve_present

    def transmit(self, bits, bases):
        if not self.eve_present:
            return bits, bases

        eve_bits = []
        eve_bases = [random.choice(['Z', 'X']) for _ in bases]

        for i in range(len(bits)):
            if eve_bases[i] == bases[i]:
                eve_bits.append(bits[i])
            else:
                eve_bits.append(random.randint(0, 1))

        return eve_bits, eve_bases
