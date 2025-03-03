from math import gcd
from random import randint

class Person:
    def __init__(self, name):
        # Simple key generation with small numbers for demonstration
        self.name = name
        # Using p=17, q=23 as example primes
        self.p = 17
        self.q = 23
        self.n = self.p * self.q  # public modulus
        self.phi = (self.p - 1) * (self.q - 1)  # Euler's totient
        self.e = 65537  # public exponent
        # Find private key d where (d * e) % phi = 1
        self.d = pow(self.e, -1, self.phi)  # private key
        
    def encrypt(self, message, recipient_e, recipient_n):
        # C = M^e mod n
        return pow(message, recipient_e, recipient_n)
    
    def decrypt(self, encrypted_msg):
        # M = C^d mod n
        return pow(encrypted_msg, self.d, self.n)

def demonstrate_encryption():
    alice = Person("Alice")
    bob = Person("Bob")
    
    # Simple message (must be number smaller than n)
    message = 42
    print(f"Original message: {message}")
    
    # Alice encrypts message using Bob's public key (e, n)
    encrypted = alice.encrypt(message, bob.e, bob.n)
    print(f"Encrypted message: {encrypted}")
    
    # Bob decrypts using his private key (d, n)
    decrypted = bob.decrypt(encrypted)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    demonstrate_encryption()