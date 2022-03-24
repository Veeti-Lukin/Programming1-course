"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def __lt__(self, other):
        """
        lower than magical method
        :param other: fraction object
        :return: bool, true if self is lower than other
        """
        if isinstance(other, Fraction):
            other_in_parts = other.return_string().split("/")
            expanded_other_numerator = int(other_in_parts[0]) * self.__denominator
            expanded_self_numerator = self.__numerator * int(other_in_parts[1])
            return expanded_self_numerator < expanded_other_numerator
        else:
            raise TypeError

    def __str__(self):
        """
        builtin print calls this magical method
        :return: str
        """
        return f"{self.__numerator}/{self.__denominator}"

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        simplifies the string by dividing both the numerator and denominator
        with greatest common divisor
        """
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)

        self.__numerator = int(self.__numerator / gcd)
        self.__denominator = int(self.__denominator / gcd)

    def complement(self):
        """
        makes a complement out of fraction by multiplying numerator by -1
        and returns new Fraction object
        :return: Fraction object
        """
        return Fraction((self.__numerator * -1), self.__denominator)

    def reciprocal(self):
        """
        makes a reciprocal out of fraction by swapping numerator and denominator
        :return: Fraction object
        """
        new_numerator = self.__denominator
        new_denominator = self.__numerator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, other):
        """
        multiplies two Fraction objects together and returns it
        :param other: Fraction object
        :return: Fraction object
        """
        if isinstance(other, Fraction):
            other_parts = other.return_string().split("/")
            new_numerator = self.__numerator * int(other_parts[0])
            new_denominator = self.__denominator * int(other_parts[1])
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("ERROR:")

    def divide(self, other):
        """
        divides this fraction object with another fraction object and returns
        new fraction object
        :param other: Fraction object
        :return: Fraction object
        """
        if isinstance(other, Fraction):
            divider = other.reciprocal()
            return self.multiply(divider)
        else:
            raise TypeError("ERROR:")

    def add(self, other):
        """
        adds fraction objects together and makes a new fraction object
        also handles the expanding
        :param other: Fraction object
        :return:fraction object
        """
        if isinstance(other, Fraction):
            other_in_parts = other.return_string().split("/")
            other_numerator = int(other_in_parts[0])
            other_denominator = int(other_in_parts[1])
            new_numerator = self.__numerator * other_denominator \
                            + other_numerator * self.__denominator
            new_denominator = self.__denominator * other_denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError

    def deduct(self, other):
        """
        deducts fraction objects from this fraction object and makes a new
        fraction object. Also handles the expanding
        :param other: Fraction object
        :return:fraction object
        """
        if isinstance(other, Fraction):
            other_in_parts = other.return_string().split("/")
            other_numerator = int(other_in_parts[0])
            other_denominator = int(other_in_parts[1])
            new_numerator = self.__numerator * other_denominator \
                            - other_numerator * self.__denominator
            new_denominator = self.__denominator * other_denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a
