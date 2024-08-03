################### Scope ####################

enemies = 1


def increase_enemies():
  global enemies
  enemies += 2
  print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope


def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()

# constant
PI = 3.14
URL = ""
