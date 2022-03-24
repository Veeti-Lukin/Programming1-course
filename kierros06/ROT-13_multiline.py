"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
ALPHABETS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
             "y", "z"]


def encrypt(character):
    """
    encrypts one character
    :param character:
    :return:
    """
    rot_version = 13

    if character.lower() in ALPHABETS:

        index = ALPHABETS.index(character.lower())
        encrypted_char = ALPHABETS[(index + rot_version) % len(ALPHABETS)]

        if character.isupper():
            encrypted_char = encrypted_char.capitalize()

        return encrypted_char
    # if character is not in alphabets
    return character


def row_encryption(text):
    """
    encrypts character array with encrypt function
    :param text: str
    :return: str, encrypted text
    """
    encrypted_text = ""
    for letter in text:
        encrypted_text += encrypt(letter)

    return encrypted_text


def read_message():
    """
    gathers user inputted text lines in a list
    :return: list, list of user inputs
    """
    list_of_inputs = []
    while True:
        user_input = input()

        if user_input == "":
            break

        list_of_inputs.append(user_input)

    return list_of_inputs


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    message = read_message()

    print("ROT13:")
    for i in message:
        print(row_encryption(i))


if __name__ == "__main__":
    main()
