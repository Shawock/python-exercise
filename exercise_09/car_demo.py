from exercise_9.car import Car
from exercise_9.car_electric import ElectronicCar

car_1 = Car('Yiqi', 'da zhong', 2015)
car_1.get_descriptive_name()

e_car_1 = ElectronicCar('Tesla', 'model s', 2015)
e_car_1.describe_battery()
print(e_car_1)
