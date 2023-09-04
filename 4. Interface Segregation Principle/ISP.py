from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self):
        print("Car started")
    def stop_engine(self):
        print("Car stopped")

class Boat(Vehicle):
    def start_engine(self):
        print("Boat started")
    def stop_engine(self):
        print("Boat stopped")
        
def test_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.stop_engine()
    
test_vehicle(Car())
test_vehicle(Boat())