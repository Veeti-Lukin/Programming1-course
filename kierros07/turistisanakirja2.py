"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

Added  line that prints the words everytime before asking for command
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    print("Dictionary contents:")
    print(", ".join(sorted(english_spanish)))

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ").upper()

        if command == "W":
            word = input("Enter the word to be translated: ").lower()

            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            word = input("Give the word to be added in English: ").lower()
            translation = input("Give the word to be added in Spanish: ").lower()

            english_spanish[word] = translation
            print("Dictionary contents:")
            print(", ".join(sorted(english_spanish)))

        elif command == "R":
            word = input("Give the word to be removed: ")

            if word in english_spanish:
                del english_spanish[word]
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "P":
            for key in sorted(english_spanish):
                print(key, english_spanish[key])

        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ")
            words = text.split()

            for index, word in enumerate(words):
                if word in english_spanish:
                    words[index] = english_spanish[word]
            print("The text, translated by the dictionary:")
            print(" ".join(words))

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
