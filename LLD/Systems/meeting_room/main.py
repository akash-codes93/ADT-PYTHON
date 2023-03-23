import threading


class Booking:

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def is_overlap(self, start_time, end_time):
        if self.start_time <= start_time <= self.end_time <= end_time:
            return True
        elif start_time <= self.start_time <= end_time <= self.end_time:
            return True
        elif self.start_time <= start_time <= end_time <= self.end_time:
            return True

        return False


class Room:
    def __init__(self, id):
        self._id = id
        self.bookings = []
        self.__lock = threading.Lock()

    @property
    def id(self):
        return self._id

    def is_room_available(self, start_time, end_time):

        for booking in self.bookings:
            if booking.is_overlap(start_time, end_time):
                return False

        return True

    def book_room(self, start_time, end_time):
        status = False
        self.__lock.acquire()
        if self.is_room_available(start_time, end_time):
            booking = Booking(start_time, end_time)
            self.bookings.append(booking)
            status = True
        self.__lock.release()
        return status

    def release_room(self, start_time, end_time):
        self.__lock.acquire()
        for _, booking in enumerate(self.bookings):
            if booking.start_time == start_time and booking.end_time == end_time:
                del self.bookings[_]
        self.__lock.release()


class Meeting:

    def __init__(self, start_time, end_time, room_id):
        self.start_time = start_time
        self.end_time = end_time
        self.room_id = room_id


class Scheduler:

    def __init__(self, rooms):
        self.rooms = rooms

    def schedule(self, start_time, end_time):
        for room in self.rooms:
            if room.is_room_available(start_time, end_time) and room.book_room(start_time, end_time):
                meeting = Meeting(start_time, end_time, room.id)
                print("Room_booked: ", room.id)
                return room.id
        print("Room not booked")
        return None


if __name__ == "__main__":
    rooms = []
    room1 = Room(1)
    room2 = Room(2)
    # room3 = Room(3)
    rooms.append(room1)
    rooms.append(room2)
    scheduler = Scheduler(rooms)
    scheduler.schedule(0, 5)
    scheduler.schedule(1, 5)
    scheduler.schedule(6, 8)
    scheduler.schedule(2, 8)