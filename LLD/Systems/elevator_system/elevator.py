import time
from typing import Dict
import threading
from collections import defaultdict
from enum import Enum
from request import RequestsDto

MAX_FLOOR = 10


class Direction(Enum):
    UP = 1
    DOWN = -1


class User:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight


class Elevator:

    def __init__(self, capacity: int, _id: int):
        self.capacity = capacity

        self.current_capacity = 0

        self.current_floor = 0
        self.dest_floor = 0
        self.start_floor = 0  # audit field

        self.is_moving = False
        self.direction = Direction.DOWN

        self.id = _id

        # floor: user
        self.users = defaultdict(list)

        # floor: [request]
        self.next_request = defaultdict(list)

        self.lock = threading.Lock()

    def add_user(self, user: User, dest_floor: int):
        self.current_capacity += user.weight
        self.users[dest_floor].append(user)

    def is_elevator_eligible(self, request: RequestsDto) -> bool:
        # make it thread safe
        with self.lock:
            if self.current_capacity + request.user.weight > self.capacity:
                print(f"Elevator {self.id} is full for user {request.user.name} at floor {request.curr_floor}")
                return False

            if self.is_moving:
                if self.direction == Direction.UP and request.curr_floor < self.current_floor:
                    print("Elevator {} is already moving upward from {} to {}".format(self.id, self.current_floor, request.curr_floor))
                    return False

                if self.direction == Direction.DOWN and request.curr_floor > self.current_floor:
                    print("Elevator {} is already moving down from {} to {}".format(self.id, self.current_floor, request.curr_floor))
                    return False

            return True

    def add_request(self, request: RequestsDto):
        # make it thread safe
        with self.lock:
            self.next_request[request.curr_floor].append(request)

    def process_requests(self):
        while True:
            with self.lock:
                self.is_moving = True
                current_floor = self.current_floor
                dest_floor = self.dest_floor

                # remove all the users from this floor
                users_to_remove = self.users[current_floor]
                for user in users_to_remove:
                    print("Elevator {} user {} has left the elevator".format(self.id, user.name))
                    self.current_capacity -= user.weight
                self.users.pop(current_floor)

                # onboard users which are present in this floor
                for request in self.next_request[current_floor]:
                    self.add_user(request.user, request.dest_floor)
                    print("Elevator {} user {} has entered the elevator".format(self.id, request.user.name))
                    self.current_capacity += request.user.weight

                # remove all the requests from this floor
                self.next_request.pop(current_floor)

                if dest_floor > current_floor:
                    self.direction = Direction.UP
                    self.current_floor += 1
                elif dest_floor < current_floor:
                    self.direction = Direction.DOWN
                    self.current_floor -= 1

                else:
                    self.is_moving = False
                    # print(self.next_request)
                    if len(self.next_request) > 0:
                        self.dest_floor = min(self.next_request.keys())
                        print("Elevator {} is moving to dest {} current {}".format(self.id, self.dest_floor, self.current_floor))
                    else:
                        print("Elevator {} is idle".format(self.id))

            time.sleep(5)

    def run(self):
        self.process_requests()