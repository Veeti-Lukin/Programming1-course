"""
COMP.CS.100 lenkkilaskuri.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

Program asks number of days from user, then asks users running length for every day separately,
after that program calculates a daily average.
"""


def number_input_manager(string, float_or_int=float):
    """
    Asks input from user with changeable question and checks if input is an positive number.

    :param string: str, question asked inside input function
    :param float_or_int: bool, changes if return value should be int or float
    :return: int, user input if it was an int
    """

    while True:
        answer = input(string)
        try:
            answer = float_or_int(answer)

            if answer >= 0:  # if positive
                return answer  # input was an positive number so we return it
                # break
            else:
                print("Input can not be negative")

        except ValueError:
            print("Bad input")  # input wasn't a number


def main():

    amount_of_days = number_input_manager("Enter the number of days: ", int)
    total_ran_length = 0
    days_without_running_count = 0  # if this gets to to 3 program should stop

    for i in range(1, amount_of_days+1):  # looping trough the days

        run = number_input_manager(f"Enter day {i} running length: ", float)
        total_ran_length += run

        if run == 0.0:  # user did not run today
            days_without_running_count += 1

            if days_without_running_count == 3:  # 3 days since last run
                print("\nYou had too many consecutive lazy days!")
                return  # program stops here
        else:
            days_without_running_count = 0

    mean = total_ran_length / amount_of_days

    if mean < 3.0:  # average person should run 3 km in a day
        print(f"\nYour running mean of {mean:.2f} km was too low!")

    else:
        print(f"\nYou were persistent runner! With a mean of {mean:.2f} km.")


if __name__ == "__main__":
    main()
