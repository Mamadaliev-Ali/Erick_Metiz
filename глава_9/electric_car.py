from car import Car


class Battery:
    """Модель аккумулятора автомобиля"""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Вывод  мощности аккумулятора"""
        print(f"This car has a {self.battery_size}-kwh battery")

    def get_range(self):
        if self.battery_size == 75:
            ranges = 260
        elif self.battery_size == 100:
            ranges = 310

        print(f"This car can go about {ranges} miles on a fill charge")

    def upgrade_battery(self, size):
        self.battery_size = size


class ElectricCar(Car):

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2022)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery(100)
my_tesla.battery.get_range()
