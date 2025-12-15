height = 9
width = 9
mines = 10

import random

randoms = random.sample(range(1, width*height), mines)
print(randoms)