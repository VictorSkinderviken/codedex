# Lets the user type in height and credit
height = int(input("Enter your height: "))
print ("Your height is", height, "cm.")
credits = int(input("Enter your credits: "))
print ("You have", credits, "tickets.")

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
# Tall enough? No. Credits enough? Yes.
elif height < 137 and credits >= 10:  
  print("You are not tall enough to ride.")
# Tall enough? Yes. Credits enough? No.
elif height >= 137 and credits < 10:  
  print("You don't have enough credits.")
# Both height < 137 and credits < 10
else:  
  print("You have not met either requirement.")