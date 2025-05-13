# Start with printing 1 to 100
for i in range(1, 101):
    # If the number divided by 3 = 0 then print Fizz
    if i % 3 == 0:
      print("Fizz")
    # If the number divided by 5 = 0 then print Bizz
    elif i % 5 == 0:
      print("Buzz")
    # If the number divided by 3 and 5, where it = 0, print FizzBuzz
    elif i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    else:
      print(i)