total = 0
for number in range(1, 101):  # range(a, b) b is exclusive
    if number % 2 == 0:
        total += number

print(total)