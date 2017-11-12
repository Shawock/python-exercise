"""一个可用于表示汽车的类"""


class Car:
    """ 这是一个用于表示车的类 """

    def __init__(self, make, model, year):
        """ init property of Car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = self.make + " " + self.model.title() + " " + str(self.year)
        print(long_name)

