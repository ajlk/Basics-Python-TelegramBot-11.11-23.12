from simplecrypt import encrypt, decrypt

with open('passwords.txt', 'r') as inp:
    passwords = inp.read().splitlines()
with open('encrypted.bin', 'rb') as inp:
    encrypted = inp.read()

for password in passwords:
    try:
        ans = decrypt(password, encrypted)
        break
    except:
        continue

print(ans)
