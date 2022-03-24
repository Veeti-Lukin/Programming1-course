"""
COMP.CS.100 Yogi bear
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:
program prints out lyrics for the song "Yogi bear".
"""


def repeat_name(bears_name, amount):
    """
    repeats the "(name), (name) bear" line (amount)amount of times

    :param bears_name: string, name of the bear in question
    :param amount: float, how many times the line is repeated
    """
    for _ in range(0, amount):
        print(f"{bears_name}, {bears_name} Bear")


def verse(lyric, bears_name):
    """
    prints out one verse.

    :param lyric: string, lyrics for this verse
    :param bears_name: string, name of the bear in question
    """
    print(lyric)
    print(bears_name+",", bears_name)
    print(lyric)
    repeat_name(bears_name, 3)
    print(lyric)
    repeat_name(bears_name, 1)


def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
