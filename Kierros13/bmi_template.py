"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Body Mass Index template
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()
        self.__mainwindow.geometry("500x200")

        self.__weight_label = Label(self.__mainwindow,
                                       text="Insert your weight(kg) here: ")
        self.__height_label = Label(self.__mainwindow,
                                       text="Insert your height(cm) here: ")

        self.__weight_value = Entry(self.__mainwindow)
        self.__height_value = Entry(self.__mainwindow)

        self.__calculate_button = Button(self.__mainwindow,
                                            text="Calculate BMI", bg="red",
                                            command=self.calculate_BMI)
        self.__result_text = Label(self.__mainwindow)
        self.__explanation_text = Label(self.__mainwindow)

        self.__stop_button = Button(self.__mainwindow, text="Quit",
                                       command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_label.grid(row=0, column=0, pady=2, padx=2)
        self.__height_label.grid(row=1, column=0, pady=2, padx=2)
        self.__weight_value.grid(row=0, column=1, pady=2, padx=2)
        self.__height_value.grid(row=1, column=1, pady=2, padx=2)
        self.__calculate_button.grid(row=2, column=0, columnspan=2, pady=2, padx=2)
        self.__result_text.grid(row=3, column=0, pady=2, padx=2)
        self.__explanation_text.grid(row=3, column=1, pady=2, padx=2)
        self.__stop_button.grid(row=4, column=0, columnspan=2, pady=10, padx=2)

    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        try:
            weight = int(self.__weight_value.get())
            height = int(self.__height_value.get())
        except ValueError:
            self.__explanation_text.configure(
                text="Error: height and weight must be numbers.")
            self.reset_fields()
            return

        if weight <= 0 or height <= 0:
            self.__explanation_text.configure(
                text="Error: height and weight must be positive.")
            self.reset_fields()
            return

        result = weight/(height/100)**2
        self.__result_text.configure(text=f"{result:.2f}")

        if result > 25:
            self.__explanation_text.configure(text="You are overweight.")
        elif result < 18.5:
            self.__explanation_text.configure(text="You are underweight.")
        else:
            self.__explanation_text.configure(text="Your weight is normal.")

    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__weight_value.delete(0, END)
        self.__height_value.delete(0, END)

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
