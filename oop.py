class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # Use consistent attribute naming
        self.nationality = "Unknown"
        
    def get_age(self):
        return self.age  # Corrected to match the constructor's attribute
    
    def set_age(self, new_age):
        if new_age > 0:
            self.age = new_age  # Use consistent attribute naming
        else:
            print("Invalid age!")

# Correct object instantiation
person = Person("Wayne", 25)

# Access attributes and methods correctly
print(person.name)
print(person.age)

print(person.get_age())
person.set_age(30)  # Changed to a different valid age
print(person.get_age())  # Verify age update
