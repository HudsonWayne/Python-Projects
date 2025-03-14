class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def driver(self):  # Change name if needed, but it's fine
        print(f"You drive the {self.model}")
        
    def stop(self):
        print(f"You stop the {self.model}")
