"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""
DAYS_OF_MONTH = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

AMOUNT_OF_MONTHS = len(DAYS_OF_MONTH)
FIRST_FRIDAY = 3  # index number of the first friday in the january


def main():

    days_of_month_values = list(DAYS_OF_MONTH.values())
    daycount = 7 - FIRST_FRIDAY

    for i in range(1, AMOUNT_OF_MONTHS+1):

        for j in range(1, days_of_month_values[i-1]+1, 7):

            daycount += 1

            if daycount == 7:
                print(f"{j}.{i}.")
                daycount = 0


if __name__ == "__main__":
    main()
