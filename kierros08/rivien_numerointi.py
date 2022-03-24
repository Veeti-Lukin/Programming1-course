"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def read_txt_file(filename):
    """
    Opens filestream to file. Reads text lines from the file adds them to list
     and closes filestream.
    :param filename: str
    :return: list, list of lines
    """
    lines = []

    try:
        file_stream = open(filename, "r")
    except OSError:
        print("ERROR: file couldn't be opened")
        return lines

    for line in file_stream:
        lines.append(line.rstrip())

    file_stream.close()
    return lines


def add_row_numbers(given_list):
    """
    adds row numbers in start of a list elements
    :param given_list: list
    :return: None
    """
    for index, value in enumerate(given_list):
        given_list[index] = f"{index+1} {value}"


def main():
    lines = read_txt_file(input("Enter the name of the file: "))
    add_row_numbers(lines)

    for i in lines:
        print(i)


if __name__ == "__main__":
    main()
