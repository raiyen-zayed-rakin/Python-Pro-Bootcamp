# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# More efficient way
# reading a file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# writing in a file
with open("my_file.txt", mode="a") as file:
    file.write(" shauwa")