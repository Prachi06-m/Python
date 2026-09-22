class LifePolicy:

    def calculate_premium(self):
        return 25000


class HealthPolicy:

    def calculate_premium(self):
        return 18000


class MotorPolicy:

    def calculate_premium(self):
        return 12000


# Different policy objects
policies = [
    LifePolicy(),
    HealthPolicy(),
    MotorPolicy()
]


# Same method, different behavior
for policy in policies:
    print(policy.calculate_premium())










# (override method frrom parent class)
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()




    