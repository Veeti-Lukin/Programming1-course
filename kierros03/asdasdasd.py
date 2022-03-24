"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
vowels = ["a", "e", "i", "o", "u", "y"]

def output_vowels(string):
    for i in string:
        if i in vowels:
            print(string[i])


def main():
    output_vowels("asdesdisdosdasfwafasdusdysd")


if __name__ == "__main__":
    main()
