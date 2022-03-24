"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
VOWELS = ["a", "e", "i", "o", "u", "y"]


def main():
    answer = input("Enter a word: ")
    amount_of_vowels = 0

    for letter in answer:
        if letter.lower() in VOWELS:
            amount_of_vowels += 1

    print(f"The word \"{answer}\" contains {amount_of_vowels} vowels "
          f"and {len(answer) - amount_of_vowels} consonants.")


if __name__ == "__main__":
    main()
