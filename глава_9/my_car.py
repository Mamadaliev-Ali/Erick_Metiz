from car import Car
from electric_car import ElectricCar as EC

my_car = Car("BMW", "M5", 2021)
print(my_car.get_descriptive_name())

my_tesla = EC("Tesla", "Model S", 2022)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print(my_tesla.get_descriptive_name())