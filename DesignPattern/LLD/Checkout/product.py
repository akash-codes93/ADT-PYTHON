from typing import Type


class Product:
    name = None
    code = None
    price = 0

    def __init__(self):
        self.discounts = []


# chai = Product("Chai", "CH1", 3.11)
# coffee = Product("Coffee", "CF1", 11.23)
# apples = Product("Apples", "AP1", 6.0)
# milk = Product("Milk", "MK1", 4.75)
# oatmeal = Product("Oatmeal", "OM1", 3.69)


class Chai(Product):
    name = 'Chai'
    code = 'CH1'
    price = 3.11


class Coffee(Product):
    name = 'Coffee'
    code = 'CF1'
    price = 11.23


class Milk(Product):
    name = 'Milk'
    code = 'MK1'
    price = 4.75


class Apples(Product):
    name = 'Apples'
    code = 'AP1'
    price = 6.00


class Oatmeal(Product):
    name = 'Oatmeal'
    code = 'OM1'
    price = 3.69


class Repository:

    def __init__(self):
        self._product_repository = {}

    def register_product(self, p: Type[Product]):
        if not issubclass(p, Product):
            print("Product should be of type class Product")
            raise Exception("Not a valid product")

        self._product_repository.update({
            p.code: p
        })

    def get_product(self, code: str) -> Product:
        try:
            product_class = self._product_repository[code]
            product = product_class()
            return product
        except KeyError:
            raise Exception("Not a valid product code")


repository = Repository()
# repository.register_product(chai)
# repository.register_product(coffee)
# repository.register_product(apples)
# repository.register_product(milk)
# repository.register_product(oatmeal)
repository.register_product(Chai)
repository.register_product(Coffee)
repository.register_product(Apples)
repository.register_product(Milk)
repository.register_product(Oatmeal)
