"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


class TankOverflowError(Exception):
    pass


class Car:
    """
    Models a car which can move a certain distance and whose tank can be filled
    and driving consumes gas
    """

    def __init__(self, tank_size, gas_consumption):
        """
        constructor initializes the object
        :param tank_size:
        :param gas_consumption:
        :attribute odometer: float, the value of odometer
        :attribute gas: float how much gas does the car have
        """
        self.__tank_volume = tank_size
        self.__consumption = gas_consumption
        self.__odometer = 0.0
        self.__gas = 0.0

    def get_odometer(self):
        """
        :return: float, the odometer value of car
        """
        return self.__odometer

    def set_odometer(self, new_value):
        """
        changes cars odometers value
        :param new_value: float, the new value of odometer
        :return: None
        """
        if new_value >= 0:
            self.__odometer = new_value
        else:
            raise ValueError(f"Setting odometer failed: must be non-negative.")

    def get_gas(self):
        """
        :return: float, the amount of gas int the car
        """
        return self.__gas

    def set_gas(self, new_value):
        """
        changes amount of gas in the car
        :param new_value: float, the new amount of gas in the car
        :return: None

        :raise TankOverflowError: if trying to change gas value to bigger
                                    number than tank volume
        """
        if new_value >= 0:
            if new_value <= self.__tank_volume:
                self.__gas = new_value
            else:
                raise TankOverflowError(
                    "Setting gas failed: value is more than tank volume")
        else:
            raise ValueError(f"Setting gas failed: must be non-negative.")

    def print_information(self):
        """
        prints cars gas status and odometer value
        :return: None
        """
        print(f"The tank contains {self.get_gas()} liters of gas "
              f"and the odometer shows {self.get_odometer()} kilometers.")

    def fill(self, amount):
        """
        adds gas to tank
        :param amount: float, how much to add
        :return:None
        """
        if amount > 0:
            try:
                self.set_gas(self.get_gas() + amount)
            except TankOverflowError:
                self.set_gas(self.__tank_volume)
        else:
            print("You cannot remove gas from the tank")

    def drive(self, distance):
        """
        consumes gas from the tank relative to distance and cars consumption
        :param distance: float, distance
        :return:None
        """
        max_distance = self.get_gas() * 100 / self.__consumption

        if distance > max_distance:
            distance = max_distance
        self.set_gas(self.get_gas() - (distance * self.__consumption/100))
        self.set_odometer(self.get_odometer() + distance)


def main():
    tank_size = read_number("How much does the vehicle's gas tank hold?")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers?")

    # Here we define the variable car which is an object initiated
    # from the class Car (its type is Car). This is the point where the
    # constructor of the class Car (i.e. the method that is named __init__)
    # is called automatically behind the scenes to give an initial
    # value for the Car object we are creating!

    car = Car(tank_size, gas_consumption)

    # In this program we only need one car object but it is possible
    # to create multiple objects from one class. For example we could
    # create more objects if we needed them:
    #
    #     lightning_mcqueen = Car(20, 30)
    #     canyonero = Car(200, 400)

    while True:
        car.print_information()

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up?")

            car.fill(to_fill)

        elif choice == "2":
            distance = read_number("How many kilometers to drive?")

            car.drive(distance)

        elif choice == "3":
            print("Thank you and bye!")
            break


def read_number(prompt, error_message="Incorrect input!"):
    """
    **** DO NOT MODIFY THIS FUNCTION ****

    This function is used to read input (float) from the user.

    :param prompt: str, prompt to be used when asking user input.
    :param error_message: str, what error message to print
        if the entered value is not a float.
    """

    while True:
        try:
            return float(input(prompt + " "))

        except ValueError:
            print(error_message)


if __name__ == "__main__":
    main()
