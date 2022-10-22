class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe(self, ):
        print("try in our restaurant " + self.type)

    def open_restaurant(self):
        print("our restaurant is " + self.name + " open ")

    def read_served(self):
        print(f"free tables: {self.number_served}")

    def set_number_served(self, number):
        self.number_served = number

    def increment_served_number(self, client):
        self.number_served += client


class IceCreamStand(Restaurant):

    def __init__(self, flavors, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def set_flavor(self):
        print(f"{self.flavors}")


cream = IceCreamStand("chocolate", "Ice Cream", "Ice")
cream.open_restaurant()
cream.describe()
cream.set_flavor()
