from dictionary_for_memo import English_words
import random, os
from RAV_hash_for_entropy import phrase_to_hash

random.seed(os.urandom(20))
choosed_words = []

for i in range (0, 12):
    choosed_words.append(random.choice(English_words))

print(phrase_to_hash(str(choosed_words)))

print(choosed_words)

random.seed(phrase_to_hash)

