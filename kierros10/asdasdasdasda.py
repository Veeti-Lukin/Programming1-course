"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
TICKET_TYPE_CHILD = "child"
TICKET_TYPE_STUDENT = "student"
TICKET_TYPE_ADULT = "adult"

TICKET_PRICE_CHILD = 1.20
TICKET_PRICE_STUDENT = 2.00
TICKET_PRICE_ADULT = 2.40


class Ticket:
    """
    A simple bus ticket.  The attributes are:
    - owner's name
    - saldo i.e. the amount of money left on a ticket
    - ticket type (child, student, adult)
    """

    def __init__(self, owner, saldo, ticket_type):
        """
        Initializes a bus ticket according to its parameters.

        :param owner: str, the name of the ticket's owner
        :param saldo: float, must be non-negative
        :param ticket_type: str, one of
               TICKET_TYPE_CHILD, TICKET_TYPE_STUDENT, or TICKET_TYPE_ADULT

        :raises: ValueError, if saldo or ticket_type is errorneous. It does not raise
                 ValueError on its own but set_saldo and set_type will do it
                 if their parameter is not acceptable.
        """

        self._set_owner(owner)
        self.set_saldo(saldo)
        self.set_type(ticket_type)

    def _set_owner(self, new_owner):
        """
        Changes the owner of the ticket.

        :param new_owner: str, the new owner of the ticket.
        """

        self.__owner = new_owner

    def get_owner(self):
        """
        :return: str, the owner of the ticket.
        """

        return self.__owner

    def get_saldo(self):
        """
        :return: float, the current amount of money stored in the ticket.
        """

        return self.__saldo

    def set_saldo(self, new_saldo):
        """
        Sets the amount of money stored on the ticket.

        :param new_saldo: float, the new amount of money on the ticket.

        :raises: ValueError, if the new_saldo is negative.
        """

        if new_saldo >= 0.0:
            self.__saldo = new_saldo
        else:
            raise ValueError(
                f"Setting saldo for {self.get_owner()} failed: must be non-negative.")

    def get_type(self):
        """
        :return: str, the type of the ticket (child, student, or adult).
        """

        return self.__type

    def set_type(self, new_type):
        """
        Changes the type of the ticket.

        :param new_type: str, the desired new type for the ticket. must be one of:
                         TICKET_TYPE_CHILD, TICKET_TYPE_STUDENT, TICKET_TYPE_ADULT

        :raises: ValueError, if the new_type's value is not one of the known ticket types.
        """

        if new_type in [TICKET_TYPE_CHILD, TICKET_TYPE_STUDENT,
                        TICKET_TYPE_ADULT]:
            self.__type = new_type
        else:
            raise ValueError(
                f"Setting type for {self.get_owner()} failed: unknown type {new_type}.")

    def printout(self):
        """
        Prints on screen the values of the attributes.
        Useful for testing purposes if not for anything else.
        """

        print(
            f"owner:{self.get_owner()} / saldo:{self.get_saldo()} / type:{self.get_type()}")

    def travel(self):
        """
        Deducts money worth one trip from the ticket's current saldo.

        :raises: ValueError, if ticket does not have enough money for the trip.
        """

        ticket_type = self.get_type()

        if ticket_type == TICKET_TYPE_CHILD:
            cost = TICKET_PRICE_CHILD
        elif ticket_type == TICKET_TYPE_STUDENT:
            cost = TICKET_PRICE_STUDENT
        else:
            cost = TICKET_PRICE_ADULT

        if self.get_saldo() < cost:
            raise ValueError(
                f"Saldo {self.get_saldo()} for {self.get_owner()} too low. Walk!")
        else:
            self.set_saldo(self.get_saldo() - cost)

    def add_money(self, amount):
        """
        Adds money (recharges) on the ticket.

        :param amount: float, the amount of money to add on the ticket's saldo.

        :raises: ValueError, if amount is not positive, since adding zero or negatice
                 amount does not make much sense.
        """

        if amount <= 0.0:
            raise ValueError(
                f"Adding money for {self.get_owner()} failed: amount must be positive.")
        else:
            self.set_saldo(self.get_saldo() + amount)


def main():
    ticket = Ticket("testityyppii66", 10, "child")
    ticket.__set


if __name__ == "__main__":
    main()
