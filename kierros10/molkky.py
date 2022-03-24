"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


class Player:
    """
    Models a player playing Mölkky

    Attributes:
        name:   str, name of the player
        points: int, how many points the player has
    """

    def __init__(self, name):
        """
        Constructor that initializes name, and points of the player.
        Raises exception if value of points is erroneous.
        :param name: str, name of the player
        :raises: ValueError, if points are lower than zero
        """
        self.set_points(0)
        self.set_name(name)
        self.__throws = []

    def get_points(self):
        """
        Getter, return amount of points
        :return: int, amount of points
        """
        return self.__points

    def set_points(self, value):
        """
        Setter, sets amount of points
        :param value: int, new amount of points
        :raises: ValueError, if trying to set negative number
        """
        if value >= 0:
            self.__points = value
        else:
            raise ValueError(
                f"ERROR: While setting  points for '{self.__name}'"
                f"cant add negative amount of points")

    def get_name(self):
        """
        Getter, returns players name
        :return: str
        """
        return self.__name

    def set_name(self, name):
        """
        Setter, sets player name
        :param name: str,
        """
        self.__name = name

    def add_points(self, amount):
        """
        Adds points for player
        :param amount: int, how much to add
        """
        self.calc_mean()

        if self.get_points() + amount <= 50:
            self.set_points(self.get_points() + amount)
            if 40 <= self.get_points() < 49:
                print(
                    f"{self.get_name()} needs only {50 - self.get_points()} points. "
                    f"It's better to avoid knocking down the pins with higher points.")
        else:
            print(f"{self.get_name()} gets penalty points!")
            self.set_points(25)

        self.__throws.append(amount)

    def has_won(self):
        """
        Retuns true if player has exactly 50 points
        :return: bool
        """
        if self.get_points() == 50:
            return True
        else:
            return False

    def calc_mean(self):
        """
        calculates mean of the throws
        :return: float, mean of the throws
        """
        try:
            return sum(self.__throws) / len(self.__throws)
        except ZeroDivisionError:
            # no throws yet
            pass

    def calc_hit_percentage(self):
        """
        calculates percentage of how many throws has hit a targets
        :return: float, percentage
        """
        hits = [x for x in self.__throws if x != 0]
        try:
            return (len(hits) / len(self.__throws)) * 100
        except ZeroDivisionError:
            # no throws yet
            return 0.0


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        if pts > in_turn.calc_mean():
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(
            f"{player1.get_name()}: {player1.get_points()} p, hit percentage",
            f"{player1.calc_hit_percentage():.1f}")
        print(
            f"{player2.get_name()}: {player2.get_points()} p, hit percentage",
            f"{player2.calc_hit_percentage():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
