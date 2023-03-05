from product import repository as product_repository
from discount import discount_repository


HEADER_SPACES = 18
SPACES = 19
PRE_PROMO_SPACES = 6
POST_PROMO_SPACES = 11


class Cart:

    def __init__(self):
        self.products = []

    def add_product(self, code):
        product = product_repository.get_product(code)
        self.products.append(product)

    @property
    def total(self):
        total = 0
        for item in self.products:
            total += item.price

            for discount in item.discounts:
                total += discount.price

        return total

    def checkout(self):

        discount_repository.apply_discounts(self.products)

        print("Item" + " " * HEADER_SPACES + 'Price')
        print("----" + " " * HEADER_SPACES + '-----')
        # print(self.item_list)
        for product in self.products:

            print(product.code + " " * SPACES + str(product.price))
            for discount in product.discounts:
                print(" " * PRE_PROMO_SPACES + discount.name + " " * POST_PROMO_SPACES + str(discount.price))

        print("--------------------------")
        print("                      " + str(round(self.total, 2)))


file1 = open('input.txt', 'r')
lines = file1.readlines()
for index, line in enumerate(lines):
    _items = [str(piece).strip() for piece in line.split(',')]
    print("\n")
    print("Test Case: " + str(index + 1))
    print("Input: {0}".format(_items))
    print("--------------------------")
    cart = Cart()
    for _item in _items:
        cart.add_product(_item)
    cart.checkout()
    print("\n")
    break
