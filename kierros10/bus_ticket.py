"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
A simple class for modelling a bus ticket.
"""

TICKET_TYPE_CHILD     = "child"
TICKET_TYPE_STUDENT   = "student"
TICKET_TYPE_ADULT     = "adult"

TICKET_PRICE_CHILD    = 1.20
TICKET_PRICE_STUDENT  = 2.00
TICKET_PRICE_ADULT    = 2.40


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

        self.set_owner(owner)
        self.set_saldo(saldo)
        self.set_type(ticket_type)

    # The following methods whose name begin with get_ or set_ are
    # often called getters and setters. Their purpose is to grant
    # direct access to the member variables. Notice though that
    # we did not use them in out test main function. It is usually
    # advisable not to call getters and setters outside the other method
    # functions. This is not an absolute rule though. More information
    # about this below in the chapter "Getter and Setter Methods"
    # (or "Getter- ja setter-metodit").

    def get_owner(self):
        """
        :return: str, the owner of the ticket.
        """

        return self.__owner

    def set_owner(self, new_owner):
        """
        Changes the owner of the ticket.

        :param new_owner: str, the new owner of the ticket.
        """

        self.__owner = new_owner

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
            raise ValueError(f"Setting saldo for {self.get_owner()} failed: must be non-negative.")

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

        if new_type in [TICKET_TYPE_CHILD, TICKET_TYPE_STUDENT, TICKET_TYPE_ADULT]:
            self.__type = new_type
        else:
            raise ValueError(f"Setting type for {self.get_owner()} failed: unknown type {new_type}.")

    def printout(self):
        """
        Prints on screen the values of the attributes.
        Useful for testing purposes if not for anything else.
        """

        print(f"owner:{self.get_owner()} / saldo:{self.get_saldo()} / type:{self.get_type()}")

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
            raise ValueError(f"Saldo {self.get_saldo()} for {self.get_owner()} too low. Walk!")
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
            raise ValueError(f"Adding money for {self.get_owner()} failed: amount must be positive.")
        else:
            self.set_saldo(self.get_saldo() + amount)


def main():
    try:
        child_ticket = Ticket("Chris Child", 10.00, TICKET_TYPE_CHILD)
        student_ticket = Ticket("Stan Student", 1.00, TICKET_TYPE_STUDENT)
        adult_ticket = Ticket("Andrew Adult", 50.00, TICKET_TYPE_ADULT)

    except ValueError as error_message:
        print(error_message)
        return


    # ----- Testing travel method -----
    child_ticket.travel()

    # Student does nothave enough money to travel,
    # let's test the behavior if that happens.
    try:
        student_ticket.travel()
    except ValueError as error_message:
        print(error_message)

    adult_ticket.travel()


    # ----- Testing add_money method -----
    child_ticket.add_money(5.00)

    # To test the behavior when an error happens we
    # will again use the student as a guinea pig.
    try:
        student_ticket.add_money(0.0)
    except ValueError as error_message:
        print(error_message)

    adult_ticket.add_money(10.00)


    # ----- Test prints: is everything correct after the test operations -----
    child_ticket.printout()
    student_ticket.printout()
    adult_ticket.printout()


if __name__ == "__main__":
    main()
