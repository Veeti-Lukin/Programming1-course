"""
COMP.CS.100 Ensimmäinen Python-ohjelma.
Tekijä: Veeti Lukin
Opiskelijanumero: 050797635

Descritpiton of the program:

"""


class Product:
    """
    models a product bought from a shop
    """
    def __init__(self, name, price):
        """
        A product object is initialized with the name and the initial price
        :param name: str, name of the product
        :param price: float, price of the product
        """
        self.__name = name
        self.__price = price
        self.__sale = 0

    def printout(self):
        """
        prints information about the product
        :return: None
        """
        print(self.__name)
        print(" price: ", self.__price)
        print(" sale%: ", self.__sale)

    def get_price(self):
        """
        returns product price including sale percentage
        :return: float
        """
        return self.__price * (1-(self.__sale/100))

    def set_sale_percentage(self, amount):
        """
        changes sale percentage
        :param amount: float, new sale percntage
        :return: None
        """
        self.__sale = amount


def main():
    test_products = {
        "milk": 1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
