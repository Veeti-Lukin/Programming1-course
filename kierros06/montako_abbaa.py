"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def count_abbas(text):
    """
    Counts how many time a word appears in text
    :param word: str, what word are we looking for
    :param text: str, text where we are looking from
    :return: int, count
    """
    word = "abba"
    word_count = 0

    for index, value in enumerate(text):
        # if the fist letter matches
        if value == word[0]:
            # taking test slice of text
            test_text = text[index:index + len(word)]
            if test_text == word:
                word_count += 1

    return word_count

def main():
    pass


if __name__ == "__main__":
    main()
