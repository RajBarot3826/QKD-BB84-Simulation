def parity(block):
    return sum(block) % 2


def error_correction(alice_key, bob_key, block_size=4):
    corrected_bob = bob_key.copy()

    for i in range(0, len(alice_key), block_size):
        a_block = alice_key[i:i + block_size]
        b_block = corrected_bob[i:i + block_size]

        if len(a_block) != len(b_block):
            continue

        if parity(a_block) != parity(b_block):
            corrected_bob[i] = alice_key[i]

    return corrected_bob
