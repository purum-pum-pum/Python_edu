from dictionary_for_memo import English_words
from RAV_prime_test import generateLargePrime, list_of_primes
from RAV_generate_private_d import bruteforse_k_for_rsa_d
import random, os
from RAV_hash_for_entropy import phrase_to_hash

random.seed(os.urandom(20))
choosed_words = []

for i in range (0, 12):
    choosed_words.append(random.choice(English_words))

print(phrase_to_hash(str(choosed_words)))

print(choosed_words)


random.seed(str(phrase_to_hash))

generateLargePrime(3086)
print(list_of_primes)

rsa_number_n = list_of_primes[1]*list_of_primes[2]
rsa_number_phi = (list_of_primes[1] - 1)*(list_of_primes[2] - 2)
rsa_number_k = bruteforse_k_for_rsa_d(rsa_number_phi, 65537)
print("prime numbers p AND q  " + str(list_of_primes[1]) + " .... " + str(list_of_primes[2]))
print("RSA n number  " + str(rsa_number_n))
print("RSA phi number  " + str(rsa_number_phi))
print("RSA k number brutforced  " + str(rsa_number_k))
