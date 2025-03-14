from car import Car  # Make sure 'car.py' is correctly named and in the same folder

car1 = Car("Mustang", 2024, "red", False)

print(car1.model)  # Should print: Mustang

car1.driver()  # Should print: You drive the Mustang
car1.stop()  # Should print: You stop the Mustang
