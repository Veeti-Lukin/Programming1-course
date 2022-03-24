"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def read_file(filename):
    """

    :param filename:
    :return:
    """
    lines = []
    try:
        file = open(filename, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return lines

    for line in file:
        lines.append(line.rstrip())
    return lines


def make_dict(given_list):
    """

    :param given_list:
    :return:
    """
    dictionary = {}

    for element in given_list:
        parts = element.split()

        try:
            name, score = parts[0].strip(), int(parts[1].strip())
        except IndexError:
            print("There was an erroneous line in the file:")
            print(element)
            return {}
        except ValueError:
            print("There was an erroneous score in the file:")
            print(parts[1])
            return {}

        if name not in dictionary:
            dictionary[name] = score
        else:
            dictionary[parts[0]] += score

    return dictionary


def main():
    filename = input("Enter the name of the score file: ")
    scores_list = read_file(filename)
    scores_dict = make_dict(scores_list)

    if scores_dict != {}:
        print("Contestant score:")
        for name in sorted(scores_dict.keys()):
            print(f"{name} {scores_dict[name]}")


if __name__ == "__main__":
    main()
