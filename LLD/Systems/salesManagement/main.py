class Item:

    def __init__(self, name, is_beverage=False):
        self.name = name
        self.is_beverage = is_beverage


class Store:

    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.city.add_city_store(self)
        self.menu = []

    class _StoreItem:

        def __init__(self, item, price, stock):
            self.item = item
            self.price = price
            self.stock = stock
            self.sold = 0

        def unit_sold(self, units):
            if units <= self.stock_left:
                self.sold += units
                return
            print(f"{self.item.name} stock not left to sold this many units")

        @property
        def stock_left(self):
            return self.stock - self.sold

    def add_item_to_menu(self, item, price, stock):
        self.menu.append(self._StoreItem(item, price, stock))

    def sell_item(self, item, sold):
        for menu_item in self.menu:
            if item == menu_item.item.name:
                menu_item.unit_sold(sold)

    def get_items_sold(self):
        sold = 0
        for store_item in self.menu:
            sold += store_item.sold
        return sold


class City:

    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.state.add_state_city(self)
        self.__stores = []

    def add_city_store(self, store):
        self.__stores.append(store)

    def get_items_sold(self):
        sold = 0
        for store in self.__stores:
            sold += store.get_items_sold()
        return sold


class State:

    def __init__(self, name):
        self.name = name
        self.__cities = []

    def add_state_city(self, store):
        self.__cities.append(store)

    def get_items_sold(self):
        sold = 0
        for city in self.__cities:
            sold += city.get_items_sold()
        return sold


def driver():

    # state
    maharashtra = State('Maharashtra')

    # city
    mumbai = City('Mumbai', maharashtra)
    nagpur = City('Nagpur', maharashtra)

    # store
    s1_m = Store('s1', mumbai)
    s2_m = Store('s2', mumbai)

    s1_n = Store('s1', nagpur)
    s2_n = Store('s2', nagpur)

    # items
    sandwich = Item('sandwich')
    poha = Item('poha')
    tea = Item('tea', True)

    # adding item to store
    s1_m.add_item_to_menu(sandwich, 100, 10)
    s2_m.add_item_to_menu(sandwich, 90, 8)

    s1_m.add_item_to_menu(poha, 50, 20)
    s2_m.add_item_to_menu(poha, 40, 30)

    s1_n.add_item_to_menu(poha, 50, 20)
    s2_n.add_item_to_menu(poha, 40, 30)

    s1_n.add_item_to_menu(tea, 10, 40)
    s2_n.add_item_to_menu(tea, 8, 50)

    # selling
    s1_m.sell_item('sandwich', 8)
    s2_m.sell_item('sandwich', 8)

    s1_m.sell_item('poha', 20)
    s2_m.sell_item('poha', 23)

    s1_n.sell_item('poha', 20)
    s2_n.sell_item('poha', 23)

    s1_n.sell_item('tea', 30)
    s2_n.sell_item('tea', 37)

    units_sold = maharashtra.get_items_sold()
    print(f"{maharashtra.name}: {units_sold}")

    units_sold = mumbai.get_items_sold()
    print(f"{mumbai.name}: {units_sold}")

    units_sold = nagpur.get_items_sold()
    print(f"{nagpur.name}: {units_sold}")


driver()
