class Car(object):
    """
    Car class
    Author : lee
    Date : 2020.03.27

    """
    # 클래스변수 => 인스턴스끼리 공유
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def __del__(self):
        print("되는겨???")
        Car.car_count -= 1

    def detail_info(self):
        print("Current id {}".format(id(self)))
        print("Car detail info : {} {}".format(
            self._details.get('horsepower'), self._details.get('price')))


car1 = Car('Ferrari', {'color': 'white1', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 500, 'price': 5000})
car3 = Car('Benz', {'color': 'Red', 'horsepower': 1000, 'price': 3000})

print(car1)
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)
for i in car_list:
    print(repr(i))

# Check id
print(id(car1))
print(id(car2))
print(id(car3))

print(car1.__dict__)

# docstring
print(car1.__doc__)

# 생성하기
car1.detail_info()
Car.detail_info(car2)

print(car1.car_count)

del car1

print(car2.car_count)
