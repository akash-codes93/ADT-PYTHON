from enum import Enum
from typing import Optional


class Location:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class QuadStatus(Enum):
    DIVIDED = 0
    FILLED_LEAF = 1
    EMPTY_LEAF = 2


class Cab:

    def __init__(self, location: Location):
        self.location = location


class Quad:

    def __init__(self, center: Location, half_width: float, half_height: float, parent: Optional['Quad'],
                 ne=None, nw=None, sw=None, se=None):
        self.center = center
        self.half_width = half_width
        self.half_height = half_height
        self.parent = parent
        self.ne = ne
        self.nw = nw
        self.sw = sw
        self.se = se

        self.cab = None
        self.quad_status = QuadStatus.EMPTY_LEAF

    def is_location_valid(self, location: Location):
        top = self.center.y + self.half_height
        bottom = self.center.y - self.half_height
        left = self.center.x - self.half_width
        right = self.center.y + self.half_width

        print("Quad Boundary: ", top, bottom, left, right)

        return all(
            (top >= location.y,  # top
             left < location.x,  # left
             bottom < location.y,  # bottom
             right >= location.x)  # bottom
        )

    def create_children(self):
        print("Creating new children")
        ne = Quad(Location(self.center.x + self.half_width / 2, self.center.y + self.half_height / 2),
                  self.half_width / 2, self.half_height / 2, self
                  )
        nw = Quad(Location(self.center.x - self.half_width / 2, self.center.y + self.half_height / 2),
                  self.half_width / 2, self.half_height / 2, self
                  )

        se = Quad(Location(self.center.x + self.half_width / 2, self.center.y - self.half_height / 2),
                  self.half_width / 2, self.half_height / 2, self
                  )
        sw = Quad(Location(self.center.x - self.half_width / 2, self.center.y - self.half_height / 2),
                  self.half_width / 2, self.half_height / 2, self
                  )

        self.ne = ne
        self.nw = nw
        self.sw = sw
        self.se = se

    def insert_quad(self, cab: Cab):
        cab_location = cab.location

        if not self.is_location_valid(cab_location):
            print("location of cab is not within quad")
            return

        if self.quad_status == QuadStatus.EMPTY_LEAF:
            print("Quad is Empty leaf")
            self.cab = cab
            self.quad_status = QuadStatus.FILLED_LEAF

        elif self.quad_status == QuadStatus.FILLED_LEAF:
            print("Quad is Filled leaf")
            self.create_children()
            self.quad_status = QuadStatus.DIVIDED
            current_cab = self.cab
            self.cab = None
            print("Cab be will be re-inserted")

            self.insert_quad(current_cab)
            self.insert_quad(cab)

        elif self.quad_status == QuadStatus.DIVIDED:

            print("Quad is divided")

            if cab_location.x >= self.center.x and cab_location.y > self.center.y:
                print("Inserting in ne")
                self.ne.insert_quad(cab)

            elif cab_location.x < self.center.x and cab_location.y >= self.center.y:
                print("Inserting in nw")
                self.nw.insert_quad(cab)

            elif cab_location.x <= self.center.x and cab_location.y < self.center.y:
                print("Inserting in sw")
                self.sw.insert_quad(cab)

            elif cab_location.x > self.center.x and cab_location.y <= self.center.y:
                print("Inserting in se")
                self.se.insert_quad(cab)

            print("Cab is Inserted")


def driver():
    center = Location(100, 100)
    quad = Quad(center, 100, 100, None)
    cab = Cab(Location(150, 150))

    quad.insert_quad(cab)
    quad.insert_quad(Cab(Location(50, 50)))


driver()
