import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ans = ""

while ans != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = int(shift % 26)


    def caeser(direct, plain_text, shift_times):
        end_text = ""
        if direct == "decode":
            shift_times *= -1
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_p = position + shift_times
                end_text += alphabet[new_p]
            else:
                end_text += char

        print(f"The {direct}d text is {end_text}")


    caeser(direction, text, shift)
    print("Restart the cipher program? no for exit, anything else for yes")
    ans = input()
print("Thank you for playing.")

# def encrypt(plain_text, shift_times):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         cipher_text += alphabet[position+shift_times]
#     print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(plain_text, shift_times):
#     dec_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         dec_text += alphabet[position-shift_times]
#     print(f"The encoded text is {dec_text}")



