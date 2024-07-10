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
data3=80000000000111111111878000000000000000000111111111878000000000000000000011111111878111111111000473873000000000000000000001111111187811111111187811111347642830000000000000000000000111111111118780000000000001111111111111111111111111111878000000000011111111111111111111878000000000000011111111110000000

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