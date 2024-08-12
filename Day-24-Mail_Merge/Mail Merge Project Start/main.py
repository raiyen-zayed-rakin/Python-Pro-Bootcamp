#TODO: Create a letter using starting_letter.txt 

with open("Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

for name in names:
    name = name.strip()
    with open("Input/Letters/starting_letter.txt", "r") as file:
        data = file.readlines()
        main_line = data[0]
        test = main_line.replace("[name]", name)
        data[0] = test
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "a") as new_file:
            for datas in data:
                new_file.write(datas)


# data = open("Input/Letters/starting_letter.txt", "r")
# test = data.readlines()
# print(test[0])


