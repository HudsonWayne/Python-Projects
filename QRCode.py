# import qrcode 

# my_qr = qrcode.make("https://www.youtube.com/watch?v=2vjPBrBU-TM&list=RDZSM3w1v-A_Y&index=10")
# my_qr.save("my_qr.png", scare = 8)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(F"{self.name} is sleeping")
        
class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

dog = Dog("Bobby")
cat = Cat("Millicent")
bird = Bird("Sparrow")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()