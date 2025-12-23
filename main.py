class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print (f'{self.brand} , {self.model} is driving')

class ElectricCar(Car):
    def __init__(self, model, brand, battery_size):
        # ใช้ super() เพื่อดึงคุณสมบัติจากคลาสแม่ (Car)
        super().__init__(model, brand)
        self.battery_size = battery_size

    def charge(self):
        print(f"The {self.battery_size}kWh battery is charging...")

my_car = Car('Toyota', 'Vios')
my_car.drive()
my_ev = ElectricCar('Tesla', 'Model 3', 75)
my_ev.drive()
my_ev.charge()

