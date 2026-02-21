#password_generator.py
import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890"
password = ""

for i in range(8):
    password += random.choice(chars)

print("Generated Password:", password)
