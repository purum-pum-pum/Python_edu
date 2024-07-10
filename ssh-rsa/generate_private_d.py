import random


for i in range(60000):

    l = int(random.getrandbits(2048))

    l11 = (l*+1)%65537
    print(l11)