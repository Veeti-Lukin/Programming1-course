"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def gather_inputs(string):
    """
    gathers a list of words from user inputs
    :param string: str, string to print
    :return: list, list of words
    """
    print(string)
    words = []

    while True:
        line = input().lower()
        if line == "":
            break
        parts = line.split()
        words += parts
        """for part in parts:
            words.append(part)
        """
    return words


def word_density_calculator(given_list, given_dict):
    """
    calculates how many times a word appears in a list
    saves that in dict
    :param given_list: list
    :param given_dict: dict
    :return: None
    """
    for word in given_list:
        if word not in given_dict:
            given_dict[word] = 1
        else:
            given_dict[word] += 1


def main():
    words = gather_inputs("Enter rows of text for word counting. Empty row to quit.")
    density = {}
    word_density_calculator(words, density)

    for word in sorted(density):
        print(f"{word} : {density[word]} times")

if __name__ == "__main__":
    main()
