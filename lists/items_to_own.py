cars = ['Toyota', 'Subaru', 'Range Rover', 'Land Rover']
cars[0] = 'Alphard'
del cars[0]
print(f"I would like to own a {cars[0]} car")
print(f"I would like to own a {cars[-1]} SUV")
print(f"I would like to own a {cars[-2]} SUV")
print(f"I would like to own a {cars[-3]} car")
cars.append('Lexus')
print(f"I would like to own a {cars[-1]} SUV")

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.insert(0, 'suzuki')
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)