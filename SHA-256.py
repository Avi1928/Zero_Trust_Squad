import hashlib

password1 = "password123"
password2 = "password123"

hashed1 = hashlib.sha256(password1.encode()).hexdigest()
hashed2 = hashlib.sha256(password2.encode()).hexdigest()

print(hashed1)  # e99a18c428cb38d5f260853678922e03
print(hashed2)  # e99a18c428cb38d5f260853678922e03  (Same hash!)
