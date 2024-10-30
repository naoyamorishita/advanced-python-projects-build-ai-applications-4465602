# new class car
class Car:
  # constructor
  def __init__(self, make, model):
    # encapsulation of attributes
    self.make = make
    self.model = model

  # method 
  def start_engine(self):
    print(f"{self.make} {self.make}'s engine is running!")

# instances
car1 = Car("Toyota", "Camry")
car2 = Car("Ford", "Mustang")

print(f"I have a {car1.make} {car1.model}")

# use method
car2.start_engine()