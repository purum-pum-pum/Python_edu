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
test_number_from_data2 = RunTest.longest_one_block_test(bin(data2)[:1000000])
test_number_from_data3 = RunTest.longest_one_block_test(bin(data3)[:1000000])

print('gferre ', test_number_from_data2)

ffgg = "True" in str(test_number_from_data2)
ffgg2 = "True" in str(test_number_from_data3)
print("  fff  ")
print("  fff  ")
print("  fff  ")
print("found text in " + str(ffgg))
print("found text in " + str(ffgg2))
print(data2)


print("  fff  ")
print("  fff  ")
print("  fff  ")
print('gferre ', RunTest.longest_one_block_test(bin(data3)[:1000000]))
print(bin(data3))


# test distance beetwin rsa_p and rsa_q primes. It shoudl bee bigger than 512bits 3351951982485649274893506249551461531869841455148098344430890360930441007518386744200468574541725856922507964546621512713438470702986642486608412251521024

