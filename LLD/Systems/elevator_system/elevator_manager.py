import time
import threading
from elevator import Elevator, User
from request import RequestsDto


class Singleton(type):
    _instance = None
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:

                if not cls._instance:
                    cls._instance = super().__call__(*args, **kwargs)

        return cls._instance


class ElevatorManager(metaclass=Singleton):

    def __init__(self):
        # maintain elevators
        # ...
        self.elevators = []

    def add_elevator(self, elevator: Elevator):
        # ...
        self.elevators.append(elevator)

    def accept_requests(self, request: RequestsDto):

        elevator_assigned = None

        for elevator in self.elevators:
            if elevator.is_elevator_eligible(request):
                elevator.add_request(request)
                elevator_assigned = elevator
                break

        if not elevator_assigned:
            print(f"No elevator available for user {request.user.name} at floor {request.curr_floor}")
        else:
            print(f"Elevator {elevator_assigned.id} assigned for user {request.user.name} at floor {request.curr_floor}")

    def start_elevators(self):
        # ...
        for _elevator in self.elevators:
            threading.Thread(target=_elevator.run).start()


if __name__ == "__main__":
    elevator = Elevator(capacity=5, _id=1)
    elevator_manager = ElevatorManager()
    elevator_manager.add_elevator(elevator)

    elevator_manager.start_elevators()
    time.sleep(2)  # wait for elevators to process requests

    user = User("John Doe", 1)

    elevator_manager.accept_requests(RequestsDto(user, 1, 3))
