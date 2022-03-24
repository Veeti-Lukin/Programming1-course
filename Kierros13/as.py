"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
from tkinter import *


class Käyttöliittymä:
    def __init__(self):
        self.__pääikkuna = Tk()

        self.__labelA = Label(self.__pääikkuna, text="A", borderwidth=2,
                              relief=GROOVE)
        self.__labelA.grid(row=1, column=1)

        self.__labelB = Label(self.__pääikkuna, text="B", borderwidth=2,
                              relief=SUNKEN)
        self.__labelB.grid(row=1, column=4, sticky=E)

        self.__korkealabel = Label(self.__pääikkuna, text="korkea",
                                   borderwidth=2, relief=RAISED)
        self.__korkealabel.grid(row=0, column=0, rowspan=3, sticky=N + S)

        self.__leveälabel = Label(self.__pääikkuna, text="leveä",
                                  borderwidth=2, relief=FLAT)
        self.__leveälabel.grid(row=0, column=1, columnspan=2, sticky=E + W)

        self.__lopetusnappi = Button(self.__pääikkuna, text="lopeta mut",
                                     command=self.lopeta)
        self.__lopetusnappi.grid(row=2, column=2)

        self.__pääikkuna.mainloop()

    def lopeta(self):
        self.__pääikkuna.destroy()


def main():
    käli = Käyttöliittymä()


if __name__ == "__main__":
    main()
