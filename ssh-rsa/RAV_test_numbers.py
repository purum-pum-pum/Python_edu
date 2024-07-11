import os, random
from FrequencyTest import FrequencyTest
from RunTest import RunTest
from Matrix import Matrix
from Spectral import SpectralTest
from TemplateMatching import TemplateMatching
from Universal import Universal
from Complexity import ComplexityTest
from Serial import Serial
from ApproximateEntropy import ApproximateEntropy
from CumulativeSum import CumulativeSums
from RandomExcursions import RandomExcursions

data2=random.getrandbits(2048)
data3=7224113977320366805991656467608552712239524665951815491755914508873697746943

print('gferre ', RunTest.longest_one_block_test(bin(data2)[:1000000]))
print("  fff  ")
print("  fff  ")
print("  fff  ")
print(data2)


print("  fff  ")
print("  fff  ")
print("  fff  ")
print('gferre ', RunTest.longest_one_block_test(bin(data3)[:1000000]))
print(bin(data3))