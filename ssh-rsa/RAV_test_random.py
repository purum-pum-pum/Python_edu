import random

list_numbers = []
def gen_numbers(num3):
    k = 0
    while k < num3:
        k=k+1
        list_numbers.append(random.randrange(100,400))    
    return list_numbers

