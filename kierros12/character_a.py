"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""


class Character:
    """
    models a game character with inventory that contains items
    """

    def __init__(self, name):
        """
        Constructor. Object is initialized with name and empty inventory
        :param name: str, name of the character
        :attribute inventory: dict, name of the item as key and quantity as payload
        """
        self.__name = name
        self.__inventory = {}

    def printout(self):
        """
        Prints information about the character
        """
        print(f"Name: {self.__name}")
        if self.__inventory == {}:
            print("  --nothing--")
        for item, quantity in sorted(self.__inventory.items()):
            print(f"  {quantity} {item}")

    def get_name(self):
        """
        Getter, returns characters name
        :return: str
        """
        return self.__name

    def give_item(self, item):
        """
        adds an < item > to characters inventory. If that item is already at least
        once in inventory changes the quantity accordingly.
        :param item: str, name of the item
        """
        if item not in self.__inventory:
            self.__inventory[item] = 0
        self.__inventory[item] += 1

    def remove_item(self, item):
        """
        Removes an < item > from characters inventory.
        :param item: str, name of the item
        :raise: ValueError, if the < item > is not found in inventory
        """
        if item in self.__inventory:
            self.__inventory[item] -= 1
            if self.__inventory[item] == 0:
                del self.__inventory[item]

    def has_item(self, item):
        """
        Checks if character hast < item > and return bool
        :return: bool
        """
        return item in self.__inventory

    def how_many(self, item):
        """
        Returns quantity of < item > in the inventory.
        :param item: str, name of the item
        :return: int, quantity
        """
        if self.has_item(item):
            return self.__inventory.get(item)
        else:
            return 0


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun",
                          "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
