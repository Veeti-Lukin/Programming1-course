"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


class Person:
    """
    This class models a person with an electronic wallet and address
    """
    def __init__(self, name, initial_money, initial_address):
        """
        A person object is initialized with the name and the initial amount of money in the wallet.
        :param name: str, name of the person
        :param initial_money: float, money when object is created
        :param initial_address: str, address of the person when the object is created
        """

        self.__name = name
        self.__money = initial_money
        self.__address = initial_address
        self.__test = "test"

    def printout(self):
        """
        prints out all of the persons data
        :return: None
        """

        print("—" * 25)
        print("Name:   ", self.__name)
        print("Wealth: ", self.__money)
        print("Address:", self.__address)
        print(self.__test)

    def add_money(self, amount):
        """
        adds wealth to a person object
        :param amount: float, how much to add
        :return: bool, True if value to add was positive, false otherwise
        """

        if amount < 0.0:
            return False
        else:
            self.__money += amount
            return True

    def make_payment(self, amount):
        """
        reduces wealth of person object
        :param amount: float, how much to reduce
        :return: bool, True if amount ot reduce was positive, False otherwise
        """

        if amount < 0.0:
            print("The price can't be negative.")
        elif amount > self.__money:
            print("You can't afford that.")
        else:
            self.__money -= amount

    def move(self, new_address):
        """
        changes person objects address
        :param new_address: str, address where person is moving
        :return:None
        """
        self.__address = new_address


def main():

    # Let's create an object of type Person, name it denzil,
    # and use to spy on Prof. Dexter's spending.
    denzil = Person("Denzil Dexter", 100.00, "320 Memorial Dr.")

    # State of Denzil
    denzil.printout()

    # Denzil moves out of a dormitory to a place of his own.
    denzil.move("20 Chestnut St.")

    # Where's Denzil after the move.
    denzil.printout()


if __name__ == "__main__":
    main()
