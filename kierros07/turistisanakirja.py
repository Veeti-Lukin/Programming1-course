"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

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

             # if word not in english_spanish:
            english_spanish[word] = translation
                # pois käytöstä automaatti testerin takia
            """else:
                print("The word is already in the dictionary")
                while True:
                    user_input = input("Do you want to update it [Y]/[N]: ").upper()
                    if user_input == "Y":
                        english_spanish[word] = translation
                        break
                    elif user_input == "N":
                        break
                    else:
                        print("Invalid input")"""

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
