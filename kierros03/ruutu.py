"""
COMP.CS.100 Programming 1
Template for task: box printing
"""


def print_box(w, h, m):
    """
    prints a box
    :param w: str, width of the box
    :param h: str, height of the box
    :param m: str, mark used to print the box
    :return: None
    """
    w = int(w)
    h = int(h)
    for height in range(0, h):
        for width in range(0, w):
            print(m, end="")
        print()


def main():
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
