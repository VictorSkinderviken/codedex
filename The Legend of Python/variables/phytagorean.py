# Make the user type in the a lenght of the a side of your triangle
a = int(input("a) Enter the lenght of a short side: "))
print("your first short side is", a, "centimiters long")
a = a **2
print("a **2 is", a)

# Make the user type in the a lenght of the b side of your triangle
b = int(input("b) Enter the lenght of another short side: "))
print("your second short side is", b, "centimiters long")
b = b **2
print("b **2 is", b)

# Formula for calculating the "c" side based on "a" and "b" is: 
# c = (a **2 + b **2)**0.5 
# OBS! (**0.5 er kvadratroten av (a **2 + b **2))
c = a + b
c = c **0.5
print("Your longest side is", c, "centimeters long")