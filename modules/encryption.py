import itertools
import string
import secrets
from hashlib import pbkdf2_hmac

class AdvancedCipher:
    def __init__(self, password, salt, shift, permutation):
        self.shift = shift
        self.permutation = permutation
        self.reverse_permutation = {v: k for k, v in permutation.items()}
        self.key = pbkdf2_hmac('sha256', password.encode(), salt, 100000)

    def caesar_cipher(self, text, shift):
        return ''.join(chr((ord(char) + shift) % 256) for char in text)

    def transposition_cipher(self, text, permutation):
        return ''.join(text[permutation.get(i, i)] for i in range(len(text)))

    def xor_cipher(self, text, key):
        return ''.join(chr(ord(char) ^ key_char) for char, key_char in zip(text, itertools.cycle(key)))
    
    def encrypt(self, plaintext):
        xor_encrypted = self.xor_cipher(plaintext, self.key)
        shifted = self.caesar_cipher(xor_encrypted, self.shift)
        transposed = self.transposition_cipher(shifted, self.permutation)
        xor_encrypted_again = self.xor_cipher(transposed, self.key)
        return xor_encrypted_again

    def decrypt(self, ciphertext):
        xor_decrypted = self.xor_cipher(ciphertext, self.key)
        untransposed = self.transposition_cipher(xor_decrypted, self.reverse_permutation)
        unshifted = self.caesar_cipher(untransposed, -self.shift)
        xor_decrypted_again = self.xor_cipher(unshifted, self.key)
        return xor_decrypted_again

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(all_characters) for _ in range(length))