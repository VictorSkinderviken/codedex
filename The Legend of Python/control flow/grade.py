# Let the user pick a number
grade = int(input("Enter your test result: "))

# Note, you fail if your score is not higher then 55
# aka you fail if you have 55 points
if grade > 55:
  print("Nice! You passed! :)")
else:
  print("Haha! You failed! :(")