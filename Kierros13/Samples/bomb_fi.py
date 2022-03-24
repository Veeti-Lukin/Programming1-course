from tkinter import *

class Pommianimaatio:
    def __init__(self):
        self.__päivityskerta = 0

        self.__pääikkuna = Tk()

        self.__pommikuvat = []
        for kuvatiedosto in ["cherrybomb-1.gif", "cherrybomb-2.gif"]:
            self.__pommikuvat.append(PhotoImage(file=kuvatiedosto))

        self.__pomminappi = Button(self.__pääikkuna, command=self.lopeta)
        self.__pomminappi.pack()

        self.päivitä_kuvaa()

        self.__pääikkuna.mainloop()

    def lopeta(self):
        self.__pääikkuna.destroy()

    def päivitä_kuvaa(self):
        self.__pomminappi.configure(image=self.__pommikuvat[self.__päivityskerta % 2])
        self.__päivityskerta += 1
        self.__pääikkuna.after(200, self.päivitä_kuvaa)


def main():
  käyttöliittymä = Pommianimaatio()


if __name__ == "__main__":
    main()
