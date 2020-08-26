dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:#looping through a tuple using a for loop
    print(f"\nThe original dimentions are {dimension}")

print("\nThe new dimensions are:")
#writing over a tuple
dimensions = (250,450)
for dimension in dimensions:
    print(dimension)