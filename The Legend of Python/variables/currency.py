# Asks user for how many pesos they have
pesos = int(input("What do you have left in pesos?: "))
# 1 pesos = 0,051 United States Dollar
pesos = pesos * 0.051
print ("Your pesos is worth", pesos, "in USD.")

# Asks user for how many soles they have
soles = int(input("What do you have left in soles?: "))
# 1 soles = 0,27 United States Dollar
soles = soles * 0.27
print ("Your soles is worth", soles, "in USD.")

# Asks user for how many reais they have
reais = int(input("What do you have left in reais?: "))
# 1 reais = 0,18 United States Dollar
reais = reais * 0.18
print ("Your reais is worth", reais, "in USD.")

# Calculate the total in USD.
usd = pesos + soles + reais
print ("You have", usd, "left after your vacations.")