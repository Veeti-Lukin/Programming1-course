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
    print("Enter rows of text. Quit by entering an empty row.")
    list_of_inputs = []
    while True:
        user_input = input()

        if user_input == "":
            break

        list_of_inputs.append(user_input)

    return list_of_inputs


def write_to_file(filestream, lines):
    """
    writes list elements to a txt file
    :param filestream: filestream
    :param lines: list, list of txt lines
    :return: None
    """

    for line in lines:
        print(line, file=filestream)


def add_row_numbers(given_list):
    """
    adds row numbers in start of a list elements
    :param given_list: list
    :return: None
    """
    for index, value in enumerate(given_list):
        given_list[index] = f"{index + 1} {value}"


def main():
    filename = input("Enter the name of the file: ")

    try:
        filestream = open(filename, mode="w")
    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    lines = read_message()
    add_row_numbers(lines)
    write_to_file(filestream, lines)

    filestream.close()
    print(f"File {filename} has been written.")


if __name__ == "__main__":
    main()
