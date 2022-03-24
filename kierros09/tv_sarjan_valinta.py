"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
PART_SEPARATOR = ";"
GENRE_SEPARATOR = ","


def read_file(filename):
    """
    reads file and makes dictionary where keys are genre names and payloads
    fitting movies
    moviename;genre1,genre2,genre3
    :param filename: str, name of the file
    :return: dict
    """
    genre_dictionary = {}

    try:
        file_object = open(filename, mode="r")

        for row in file_object:
            parts = row.strip().split(PART_SEPARATOR)
            movie, genre_list = parts[0], parts[1].split(GENRE_SEPARATOR)

            for genre in genre_list:
                if genre not in genre_dictionary:
                    genre_dictionary[genre] = []
                genre_dictionary[genre].append(movie)

        file_object.close()
        return genre_dictionary

    except OSError:
        print("Error: the file could not be read.")
        return None

    except ValueError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")
    genre_data = read_file(filename)

    if genre_data is None:
        return

    print(f"Available genres are: {', '.join(sorted(genre_data.keys()))}")

    while True:
        asked_genre = input("> ")
        if asked_genre in genre_data:
            for movie in sorted(genre_data[asked_genre]):
                print(movie)
        elif asked_genre == "exit":
            return
        """else:
            print("ERROR: Invalid genre.")"""


if __name__ == "__main__":
    main()
