from abc import ABC, abstractmethod


class DriveStrategy(ABC):

    @abstractmethod
    def drive(self):
        pass


class NormalDriveStrategy(DriveStrategy):

    def drive(self):
        print("This car can be driven normally")


class SpecialDrivingStrategy(DriveStrategy):

    def drive(self):
        print("This car has special driving speciality")


class Vehicle:

    def __init__(self, drive_strategy=NormalDriveStrategy()):
        self.drive_strategy = drive_strategy

    def drive(self):
        self.drive_strategy.drive()


class OffRoadVehicle(Vehicle):
    pass


class NormalVehicle(Vehicle):
    pass


if __name__ == "__main__":
    normal_driving_strategy = NormalDriveStrategy()
    normal_vehicle = NormalVehicle(normal_driving_strategy)
    normal_vehicle.drive()
