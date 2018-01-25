from exercise_09.car import Car


class Battery:
    def __init__(self, battery=70):
        self.battery = battery

    def __str__(self, *args, **kwargs):
        return "battery[" + str(self.battery) + "-kWh]"

    def describe_battery(self):
        print("now the car's battery: " + str(self.battery))

    def get_range(self):
        if self.battery < 50:
            battery_range = 100
        elif self.battery < 100:
            battery_range = 200
        else:
            battery_range = 300
        print("the car has range: " + str(battery_range))


class ElectronicCar(Car):
    def __init__(self, make, model, year):
        self.length = 0
        self.battery = Battery()

    def describe_battery(self):
        print("the car's battery: " + str(self.battery))

    def increment_length(self, length):
        if length > 0:
            self.length += length
        else:
            print("the car cannot increment minus length.")

    def __str__(self, *args, **kwargs):
        return self.make + " " + self.model.title() + " " + str(self.year) + " " + str(self.battery)
