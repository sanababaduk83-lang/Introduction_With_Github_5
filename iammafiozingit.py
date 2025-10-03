import random
import string

def random_letters():
    while True:
        yield random.choice(string.ascii_lowercase)

gen = random_letters()
for _ in range(87877842348):
    print(next(gen), end=" ")
  #дужеее багато букв...