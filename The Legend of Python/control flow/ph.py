# Makes the user type in a pH value
ph = int(input("Enter a pH value (0-14): "))

# Forces user to input a number from 0 to 14
while ph < 0 or ph > 14:
  print("Invalid input. Please enter a number between 0 and 14: ")
  ph = int(input("Enter a pH value (0-14): "))

if ph > 7:
  print ("The pH value", ph, "is basic.")
elif ph < 7:
  print ("The pH value", ph, "is acidic")
else:
  print ("The pH value", ph, "is neautral")