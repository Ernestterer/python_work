numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,101,2))
print(len(even_numbers))

odd_numbers = list(range(1,12,2))
print(odd_numbers)

square_numbers = []
for square in range(1,11):
    square_numbers.append(square**2)#all squares betweeen 1 and 10.

print(square_numbers)
#using list comprehension for the same would like like below
squares = [value**2 for value in range(1,11)]
print(squares)