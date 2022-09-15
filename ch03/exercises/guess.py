import random

x = random.randint(1, 10)
print(x)

# guessnum = int(input("Input a number between 1 - 10: "))
chances = 3

for i in range(chances):
  guessnum = int(input("Input a number between 1 - 10: "))
  if guessnum == x:
    print("Correct!")
    break
  elif guessnum > x:
    print("Too High!")
  elif guessnum < x:
    print("Too low!")
