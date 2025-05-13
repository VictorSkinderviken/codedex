import random

# Generates a random number that's either 0 or 1
num = random.randint(0, 1)   

if num > 0.5:
  print('Heads')
else:
  print('Tails')