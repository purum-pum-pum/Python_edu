import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

salt = os.urandom(16)
# derive

kdf = Scrypt(

    salt=salt,
    length=32,
    n=2**16,
    r=8,
    p=3,
)

key = kdf.derive(b"my gre2 de3e3 r43few 44password")

print(key)
# verify

kdf = Scrypt(

    salt=salt,
    length=32,
    n=2**16,
    r=8,
    p=3,

)

kdf.verify(b"my gre2 de3e3 r43few 44password", key)
