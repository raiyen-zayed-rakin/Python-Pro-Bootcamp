row1 = ["*️⃣", "*️⃣", "*️⃣"]
row2 = ["*️⃣", "*️⃣", "*️⃣"]
row3 = ["*️⃣", "*️⃣", "*️⃣"]

Map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
print()
position = input("Where do you want to put the treasure? ")

row = int(position[0]) - 1
col = int(position[1]) - 1

Map[row][col] = " X"


print(f"{row1}\n{row2}\n{row3}")


