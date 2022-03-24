"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game.
"""


class Character:
    """
    models a game character with inventory that contains items and what the
    character can do
    """

    def __init__(self, name, hitpoints):
        """
        Constructor. Object is initialized with name amount of hitpoints
        and empty inventory
        :param name: str, name of the character
        :param hitpoints: int, amount of hitpoints the character has
        :attribute inventory: dict, name of the item as key and quantity as payload
        """
        self.__name = name
        self.__hitpoints = hitpoints
        self.__inventory = {}

    def printout(self):
        """
        Prints information about the character
        """
        print(f"Name: {self.__name}")
        print(f"Hitpoints: {self.__hitpoints}")
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

    def pass_item(self, item, target):
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """
        if not isinstance(target, Character):
            return False
        if not self.has_item(item):
            return False

        self.remove_item(item)
        target.give_item(item)
        return True

    def take_damage(self, amount):
        """
        Reduces characters hitpoints.
        :param amount: int,
        """
        self.__hitpoints -= amount

    def get_hitpoints(self):
        """
        Getter. Returns amount of hitpoints character has
        :return: int
        """
        return self.__hitpoints

    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        :raise: TypeError, if trying to attack anything else than a character object
        """
        if weapon not in WEAPONS:
            print(f"Attack fails: unknown weapon \"{weapon}\".")
            return False
        if weapon not in self.__inventory:
            print(
                f"Attack fails: {self.get_name()} doesn't have \"{weapon}\".")
            return False
        if target is self:
            print(f"Attack fails: {self.get_name()} can't attack him/herself.")
            return False
        if not isinstance(target, Character):
            raise TypeError

        damage_amount = WEAPONS.get(weapon)
        target.take_damage(damage_amount)
        print(f"{self.get_name()} attacks {target.get_name()} delivering "
              f"{damage_amount} damage.")

        if target.get_hitpoints() <= 0:
            print(
                f"{self.get_name()} successfully defeats {target.get_name()}.")

        return True


WEAPONS = {
    # Weapon          Damage
    # --------------   ------
    "elephant gun": 15,
    "gun": 5,
    "light saber": 50,
    "sword": 7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)

    # Testing the pass_item method
    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()

    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword")  # Conan doesn't have a sword.
    conan.attack(conan, "gun")  # A character is not allowed to attack himself.
    conan.attack(conan, "pen")  # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")  # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword")  # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")  # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
