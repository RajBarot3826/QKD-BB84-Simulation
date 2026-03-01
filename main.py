from alice import Alice
from bob import Bob
from channel import QuantumChannel
from error_correction import error_correction
from privacy_amplification import privacy_amplification
import random


def sift_keys(alice_bits, alice_bases, bob_bits, bob_bases):
    sifted_alice = []
    sifted_bob = []

    for a_bit, a_base, b_bit, b_base in zip(alice_bits, alice_bases, bob_bits, bob_bases):
        if a_base == b_base:
            sifted_alice.append(a_bit)
            sifted_bob.append(b_bit)

    return sifted_alice, sifted_bob


def calculate_qber(alice_key, bob_key):
    errors = sum(a != b for a, b in zip(alice_key, bob_key))
    return errors / len(alice_key)


def main():

    n_bits = 100
    eve_present = True

    print("===== BB84 Quantum Key Distribution Simulation =====")

    alice = Alice(n_bits)
    bob = Bob(n_bits)
    channel = QuantumChannel(eve_present)

    alice_bits, alice_bases = alice.send_qubits()

    transmitted_bits, transmitted_bases = channel.transmit(alice_bits, alice_bases)

    bob_bits = bob.measure(transmitted_bits, transmitted_bases)

    sifted_alice, sifted_bob = sift_keys(
        alice_bits, alice_bases,
        bob_bits, bob.bases
    )

    print("Sifted Key Length:", len(sifted_alice))

    qber = calculate_qber(sifted_alice, sifted_bob)
    print("QBER:", qber)

    if qber > 0.25:
        print("Eavesdropping detected! Abort communication.")
        return

    corrected_bob = error_correction(sifted_alice, sifted_bob)

    final_key = privacy_amplification(corrected_bob)

    print("Final Secure Key (SHA-256):")
    print(final_key)


if __name__ == "__main__":
    main()
