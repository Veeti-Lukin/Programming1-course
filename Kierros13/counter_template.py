"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:       Xxxx Yyyyyy
Email:      xxxx.yyyyyy@tuni.fi

Code template for counter program.
"""

import tkinter as tk


class Counter:
    """
    Models a GUI counter which value u can increase and decrease.
    """
    def __init__(self):
        """
        Constructor. Object is initialized with graphical API and value attribute as 0
        """
        # counters value
        self.__value = 0

        # root window
        self.__root_window = tk.Tk()
        self.__root_window.title("DigitalCounter")
        self.__root_window.resizable(0, 0)

        # setting up the grid
        self.__root_window.columnconfigure(2, weight=1)
        self.__root_window.rowconfigure(3, weight=1)

        # Label displaying the current value of the counter.
        self.__current_value_label = tk.Label(self.__root_window, text=self.__value)
        self.__current_value_label.grid(row=1, column=1, columnspan=2, sticky=tk.W+tk.E)

        # Button which increases the value of the counter by one.
        self.__increase_button = tk.Button(self.__root_window, text="Increase",
                                           command=self.increase_value)
        self.__increase_button.grid(row=2, column=1, sticky=tk.W+tk.E)

        # Button which decreases the value of the counter by one.
        self.__decrease_button = tk.Button(self.__root_window, text="Decrease",
                                           command=self.decrease_value)
        self.__decrease_button.grid(row=2, column=2, sticky=tk.W+tk.E)

        # Button which resets counter to zero.
        self.__reset_button = tk.Button(self.__root_window, text="Reset",
                                        command=self.reset_value)
        self.__reset_button.grid(row=3, column=1, sticky=tk.W+tk.E)

        # Button which quits the program.
        self.__quit_button = tk.Button(self.__root_window, text="Quit", bg="red",
                                       command=self.close)
        self.__quit_button.grid(row=3, column=2, sticky=tk.W+tk.E)

        self.__root_window.mainloop()

    def close(self):
        """
        Ends eventloop and closes GUI
        """
        self.__root_window.destroy()

    def increase_value(self, amount=1):
        """
        Increases value attribute of the counter by *amount*
        Refreshes the value inside the gui.
        :param amount: int, how much to add to the value
        """
        self.__value += amount
        self.__current_value_label.configure(text=self.__value)

    def decrease_value(self, amount=1):
        """
        Decreases value attribute of the counter by *amount*
        Refreshes the value inside the gui.
        :param amount: int, how much to add to the value
        """
        self.__value -= amount
        self.__current_value_label.configure(text=self.__value)

    def reset_value(self):
        """
        Reset value attribute of the counter back to 0
        Refreshes the value inside the gui.
        """
        self.__value = 0
        self.__current_value_label.configure(text=self.__value)


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
