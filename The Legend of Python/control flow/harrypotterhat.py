# Set variables to 0
slytherin = 0
hufflepuff = 0
ravenclaw = 0
gryffindor = 0

# User inputs answer1
print ("Q1) Do you like Dawn or Dusk? ")
print ("    1) Dawn")
print ("    2) Dusk")
answer1 = int(input('Enter your answer (1-2): '))
print("\n")

# Add points based on answer1
if answer1 == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer1 == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print ("Wrong input.")

# User inputs answer2
print ("Q2) When I’m dead, I want people to remember me as: ")
print ("    1) The Good")
print ("    2) The Great")
print ("    3) The Wise")
print ("    4) The Bold")
answer2 = int(input('Enter your answer (1-4): '))
print("\n")

# Add points based on answer2
if answer2 == 1:
  hufflepuff += 2
elif answer2 == 2:
  slytherin += 2
elif answer2 == 3:
  ravenclaw += 2
elif answer2 == 4:
  gryffindor += 2
else:
  print ("Wrong input.")

# User inputs answer3
print ("Q3) Which kind of instrument most pleases your ear? ")
print ("    1) The violin")
print ("    2) The trumpet")
print ("    3) The piano")
print ("    4) The drum")
answer3 = int(input('Enter your answer (1-4): '))
print("\n")

# Add points based on answer3
if answer3 == 1:
  slytherin += 4
elif answer3 == 2:
  hufflepuff += 4
elif answer3 == 3:
  ravenclaw += 4
elif answer3 == 4:
  gryffindor += 4
else:
  print ("Wrong input.")

# Finds out house with most points
house = max(slytherin, hufflepuff, ravenclaw, gryffindor)

# Prints the winning house
if house == slytherin:
  print ("Slytherin won!")
  print("\n")
elif house == hufflepuff:
  print ("Hufflepuff won!")
  print("\n")
elif house == ravenclaw:
  print ("Ravenclaw won!")
  print("\n")
elif house == gryffindor:
  print ("Gryffindor won!")
  print("\n")
else:
  print ("Error")

# Asks user to see full scores
print ("Would you like to see the full scores on all houses?")
answer4 = input('Enter your answer (y or n): ')
print("\n")

# If yes, then print board
if answer4 == "y":
  print ("=====================================================")
  print ("You´r stats:")
  print ("=====================================================")
  print ("Slytherin:", slytherin)
  print ("Hufflepuff:", hufflepuff)
  print ("Ravenclaw:", ravenclaw)
  print ("Gryffindor:", gryffindor)
  print ("=====================================================")
elif answer4 == "n":
  print ("Okay! Thank you for doing the Quiz!")
else:
  print ("Wrong input.")