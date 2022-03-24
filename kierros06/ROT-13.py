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

def main():

    while True:
        print(row_encryption(input()))


if __name__ == "__main__":
    main()
