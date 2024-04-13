"""
order and transporter service

avoid if else in base class to decide which transporter needs to be used
instead inject that as dependency


original: https://github.com/edisnezir/factory-pattern-order/

"""
from abc import ABC, abstractmethod


class Order:

    def __init__(self, distance: int, weight: int, urgent: bool):
        self.distance = distance
        self.urgent = urgent
        self.weight = weight

    def __str__(self):
        return f"Order details distance: {str(self.distance)}, weight: {str(self.weight)}, urgent: {str(self.urgent)}"


class Transporter(ABC):

    def __int__(self, order: Order):
        self.order = order

    @abstractmethod
    def is_suitable_with_order(self) -> bool:
        pass

    @abstractmethod
    def transport(self):
        pass

    @classmethod
    def get_transporter(cls, order: Order):

        # find all subclasses that implements this abstract class
        for sub_cls in cls.__subclasses__():
            # create object of these classes by passing in the order
            obj = sub_cls()
            obj.order = order

            # checking if class is suitable to deliver
            if obj.is_suitable_with_order():
                return obj

        raise NotImplementedError("cannot find a suitable transporter")


class SeaWayTransporter(Transporter):

    def is_suitable_with_order(self) -> bool:
        return (not self.order.urgent) and self.order.distance >= 1000 and self.order.weight > 100

    def transport(self):
        print("Transporting via seaway")


class AirwayTransporter(Transporter):

    def is_suitable_with_order(self) -> bool:
        return self.order.urgent or self.order.distance >= 1000 and self.order.weight <= 100

    def transport(self):
        print("Transporting via airway")


class HighWayTransporter(Transporter):

    def is_suitable_with_order(self) -> bool:
        return (not self.order.urgent) and self.order.distance < 1000

    def transport(self):
        print("Transporting via highway")


order_list = [
    {
        "urgent": False,
        "distance": 100,
        "weight": 50
    },
    {
        "urgent": False,
        "distance": 2000,
        "weight": 4000
    },
    {
        "urgent": False,
        "distance": 1100,
        "weight": 5
    },
    {
        "urgent": False,
        "distance": 1100,
        "weight": 5
    }
]

for each_order in order_list:
    order_obj = Order(**each_order)
    transporter = Transporter.get_transporter(order_obj)
    print("-" * 20)
    print(order_obj, end=" ")
    transporter.transport()
