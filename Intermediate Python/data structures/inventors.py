# Makes a dictionary
linux = {
  'name': 'Linus Torvalds', 
  'system': 'GNU Linux',
  'plus': 'Git'

}

microsoft = {
  'name': 'Bil gates', 
  'system': 'Windows',
  'plus': 'Xbox'
}

apple = {
  'name': 'Steve Jobs', 
  'system': 'MacOS',
  'plus': 'iPhone'
}

# Update the apple dictionary
apple["plus"] = "iPhone and iPad"

print("Name:", linux["name"])
print("Known for:", linux["system"])
print ("Also known for:", linux["plus"])

print("\n")

print("Name:", microsoft["name"])
print("Known for:", microsoft["system"])
print ("Also known for: The", microsoft["plus"])

print("\n")

print("Name:", apple["name"])
print("Known for:", apple["system"])
print ("Also known for: The", apple["plus"])



