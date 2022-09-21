class Vehicle1:
    def __init__(self, brand, model, typeof, fuel_level, full_tank, tank_size):
        self.brand = brand
        self.model = model
        self.typeof = typeof
        self.tank_size = tank_size
        self.fuel_level = fuel_level
        self.full_tank = full_tank

    def Get_fuel(self):
        print("Current fuel level is: ", self.fuel_level)

    def Update_fuel_tank(self):
        amt = int(input("Enter the amount of fuel to be filled: "))
        if amt > 500:
            print("Warning fuel_level is exceeding the capacity of the tank.")
        fuel = self.fuel_level + amt
        print("Fuel now:", fuel)
        if fuel <= 300:
            print("Fuel will be in Low Level")

    def fulltank(self, fuel_level, tank_size):
        if fuel_level >= tank_size:
            print("Tank is full ")

    def drive(self):
        print(f"Hello Im driving {brand}\'s {model} ")


class Vehicle2(Vehicle1):
    def drive(self):
        print(f"Hello Im driving {self.brand}\'s {self.model} ")


brand = input("Enter the brand name: ")
model = input("Enter the model: ")
typeof = input("Enter the type of vehicle: ")
tank_size = input("Enter the vehicles tank size in fuel price: ")


a1 = Vehicle1(brand, model, typeof, full_tank=0, tank_size=0, fuel_level=0)
a1.Get_fuel()
a1.Update_fuel_tank()
a2 = Vehicle2(brand, model, typeof, full_tank=0, tank_size=0, fuel_level=0)
print("The model is:", a2.model)
a2.drive()
