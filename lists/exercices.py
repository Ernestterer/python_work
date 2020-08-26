numbers = [number for number in range(1,21) ]#list comprehension
print(numbers)

numbers = []
for number in range(1,21):
    numbers.append(number)
print(numbers)

numbers = [number for number in range(1,1_000_001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#list of multiples of 3 from 3
multiples_of_3 = [multiple for multiple in range(3,31,3)]
print(multiples_of_3)

cubes = [cube**3 for cube in range(1,11)]
print(cubes)