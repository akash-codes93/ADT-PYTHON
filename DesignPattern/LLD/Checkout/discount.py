import abc
from typing import Type

from product import *


class Discount(abc.ABC):
    name = None

    @abc.abstractmethod
    def apply_discount(self, cart):
        pass


class BOGO(Discount):
    name = 'BOGO'
    price = -Coffee.price

    def apply_discount(self, products):
        total_coffee = 0
        for product in products:
            if product.code == Coffee.code:
                total_coffee += 1
                if total_coffee % 2 == 0:
                    product.discounts.append(self)


class APPL(Discount):
    name = 'APPL'
    price = -Apples.price + 4.5

    def apply_discount(self, products):
        total_apples = 0
        for product in products:
            if product.code == Apples.code:
                total_apples += 1

        if total_apples >= 3:
            for product in products:
                if product.code == Apples.code:
                    product.discounts.append(self)


class CHMK(Discount):
    name = 'CHMK'
    price = -Milk.price

    def apply_discount(self, products):
        total_chai = 0
        for product in products:
            if product.code == Chai.code:
                total_chai += 1

        for product in products:
            if product.code == Milk.code and total_chai:
                product.discounts.append(self)
                total_chai -= 1


#
# class APOM(Discount):
#     name = 'APOM'


class Repository:

    def __init__(self):
        self._discount_repository = []

    def register_discount(self, d: Type[Discount]):
        if not issubclass(d, Discount):
            print("Product should be of type class Product")
            raise Exception("Not a valid product")

        self._discount_repository.append(d)

    def apply_discounts(self, products):
        for discount in self._discount_repository:
            discount().apply_discount(products)


discount_repository = Repository()
discount_repository.register_discount(BOGO)
discount_repository.register_discount(CHMK)
discount_repository.register_discount(APPL)
