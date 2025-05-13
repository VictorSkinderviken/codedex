# Vi starter med å printe 1-100
for i in range(1, 101):
    # Hvis i kan deles med 3 og bli 0 print Fizz
    if i % 3 == 0:
      print("Fizz")
    # Hvis i kan deles med 5 og bli 0 print Buzz
    elif i % 5 == 0:
      print("Buzz")
    # Hvis i kan deles med 5 OG 3, hvor begge blir 0 print FizzBuzz
    elif i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    else:
      print(i)