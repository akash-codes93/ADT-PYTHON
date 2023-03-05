from enum import Enum

AMOUNT_PER_KM = 20
EXTRA_SEAT_CHARGE = 0.75
PREFERRED_EXTRA_SEAT_CHARGE = 0.5
PREFERRED_RIDER_CRITERIA = 0


class Person:

    def __init__(self, name):
        self.name = name


class Driver(Person):
    pass


class RideStatus(Enum):
    NOT_STARTED = 1
    STARTED = 2
    WITHDRAWN = 3
    COMPLETED = 4


class PreferredRider(Enum):
    YES = True
    NO = False


class Ride:

    def __init__(self, id, origin, destination, no_of_seats):

        self._id = id
        self._origin = origin
        self._destination = destination
        self._no_of_seats = no_of_seats

        self._status = RideStatus.NOT_STARTED
        self._preferred_rider = PreferredRider.NO

    @property
    def id(self):
        return self._id

    @property
    def origin(self):
        return self._origin

    @property
    def destination(self):
        return self._destination

    @property
    def no_of_seats(self):
        return self._no_of_seats

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def preferred_rider(self):
        return self._preferred_rider

    @preferred_rider.setter
    def preferred_rider(self, rider):
        self._preferred_rider = rider

    @property
    def amount(self):
        print(self.preferred_rider.value)
        if self.no_of_seats >= 2:
            if self.preferred_rider.value:
                return (self.destination - self.origin) * PREFERRED_EXTRA_SEAT_CHARGE * AMOUNT_PER_KM * self.no_of_seats
            else:
                return (self.destination - self.origin) * EXTRA_SEAT_CHARGE * AMOUNT_PER_KM * self.no_of_seats
        else:
            if self.preferred_rider.value:
                return (self.destination - self.origin) * AMOUNT_PER_KM * EXTRA_SEAT_CHARGE
            else:
                return (self.destination - self.origin) * AMOUNT_PER_KM


class Rider(Person):

    def __init__(self, name):
        super().__init__(name)

        self._rides = {}
        self.completed_rides = []

    def create_ride(self, id, origin, dest, seats):
        ride = Ride(id, origin, dest, seats)
        self._rides.update({
            id: ride
        })

        ride.status = RideStatus.STARTED

        if len(self.completed_rides) > PREFERRED_RIDER_CRITERIA:
            ride.preferred_rider = PreferredRider.YES

    def update_ride(self, id, origin, dest, seats):
        ride = self._rides.pop(id)
        ride.id = id
        ride.origin = origin
        ride.destination = dest
        ride.no_of_seats = seats

        self._rides.update({
            id: ride
        })

    def withdraw_ride(self, id):
        ride = self._rides[id]
        ride.status = RideStatus.WITHDRAWN

    def close_ride(self, id):
        ride = self._rides.pop(id)
        ride.status = RideStatus.COMPLETED
        self.completed_rides.append(ride)
        return ride.amount


rider = Rider("akash")

rider.create_ride(1, 50, 60, 1)
amount = rider.close_ride(1)
print(amount)

rider.create_ride(2, 50, 60, 2)
amount = rider.close_ride(2)
print(amount)
