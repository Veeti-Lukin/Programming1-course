"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
def change_value(matrix):
    pass

def main():

    matrix = [[0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]

    for i in range(len(matrix)):
        for j in matrix[i]:
            print(f"{j:^3}", end="")
        print()


if __name__ == "__main__":
    main()
