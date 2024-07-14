import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

salt = os.urandom(16)
# derive

def phrase_to_hash(some_wods):
    kdf = Scrypt(

    salt=str.encode("56"),
    length=128,
    n=2**16,
    r=8,
    p=3,
    )
    
    key = kdf.derive(str.encode(some_wods))
    
    print(key.hex())

    kdf = Scrypt(

    salt=str.encode("56"),
    length=128,
    n=2**16,
    r=8,
    p=3,
    )

    kdf.verify(str.encode(some_wods), key)

    return key.hex()

#phrase_to_hash("hhhh r5g6 hhggffxerctv55 kkii99kh7yy7 h7hy7y7oiu8uuu8u hyybby")