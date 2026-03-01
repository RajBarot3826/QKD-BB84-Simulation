import hashlib

def privacy_amplification(key):
    key_str = ''.join(map(str, key))
    hashed = hashlib.sha256(key_str.encode()).hexdigest()
    return hashed
