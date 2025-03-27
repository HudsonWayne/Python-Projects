from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass 
    
    @abstractmethod
    def stop(self):
        pass
    
    
class Car(Vehicle):
    def go(self):
        print("You drive the car")
    
car = Car()
car.go()
car.stop()