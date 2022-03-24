"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


def read_file(filename):
    """
    Reads csv file and makes a dictionary
    key;fact1;fact2;.....factn
    Assumes first line to be column headers
    :param filename:str, name of the csv file
    :return:dict
    """
    separator_mark = ";"
    info = {}
    try:
        file_object = open(filename, mode="r")

        for line_num, line in enumerate(file_object):
            # name has been taken out
            facts, name = line.strip().split(separator_mark)[1:],\
                    line.strip().split(separator_mark)[0]

            # reading and saving headers
            if line_num == 0:
                column_headers = facts[:]
                continue

            fact_dict = {}

            for fact_num, fact in enumerate(facts):
                fact_dict[column_headers[fact_num]] = fact

            info[name] = fact_dict

        return info

    except OSError:
        print("ERROR: file couldn't be opened")
        return None


def main():
    print(read_file("contacts.csv"))


if __name__ == "__main__":
    main()
