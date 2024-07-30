import random

print("Enter names:")
names = input()
name_list = names.split(", ")

# random_index = random.randint(0, len(name_list)-1)
person_who_pays = random.choice(name_list)

print(type(person_who_pays))

print(f"{person_who_pays} is going to buy the meal today!")


