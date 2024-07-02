import os
import binascii

# Generate a random secret key in binary and convert it to hexadecimal
secret_key = binascii.hexlify(os.urandom(24)).decode()
print(secret_key)
print(binascii.hexlify(os.urandom(24)).decode())