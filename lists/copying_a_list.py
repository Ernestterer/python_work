my_foods = ['avocado', 'banana', 'mango', 'manaa']
my_friends_food = my_foods[:]#coppy my_foods list

my_foods.append('chapo')
my_friends_food.append('mayai')

print(f"My best foods are : {my_foods}\n")
for food in my_friends_food:
    print(f"My best friends foods are: {food}")
