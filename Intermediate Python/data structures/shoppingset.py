# Creates set1
set1 = {"Strawberry", "Broccoli","Banana"}
set2 = {"Avocado", "Broccoli", "Tomatos"}

# .add() method adds one new item to a set. If that item already exists, nothing happens.
set1.add("Corn")

# .remove() method removes an item from a set if it exists.
set2.remove("Avocado")

# .union(): Combines two or more sets and returns a new set.
union_result = set1.union(set2)

# .intersection(): Returns a set of items common to two or more sets.
intersection_result = set1.intersection(set2)

# .difference(): Returns a set of items found only in the calling set.
difference_result = set1.difference(set2)

print("Union:")
print(union_result)
print("Intersection:")
print(intersection_result)
print("Difference:")
print(difference_result)