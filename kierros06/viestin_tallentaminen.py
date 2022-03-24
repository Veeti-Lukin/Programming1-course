"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


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

    print("The same, shouting:")
    for i in message:
        print(i.upper())


if __name__ == "__main__":
    main()
