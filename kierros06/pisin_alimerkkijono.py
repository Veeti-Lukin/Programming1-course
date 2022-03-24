"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def longest_substring_in_order(text):
    """
    finds longest substring that follows ASCII encoding from a text
    :param text:
    :return:
    """
    # if there is only one letter in the text
    if len(text) < 1:
        return text

    longest_word = text[0]
    test_word = text[0]
    text = text.casefold()

    for value in text:
        # if current character comes after the last character
        if value > test_word[-1]:
            test_word += value
            # check if current word is longer than the longest
            if len(test_word) > len(longest_word):
                longest_word = test_word
        else:
            test_word = value

    return longest_word


def main():
    print(longest_substring_in_order(input()))


if __name__ == "__main__":
    main()
