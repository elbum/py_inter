class Car(object):
    """
    Car class
    Author : lee
    Date : 2020.03.27

    Class , Static , Instance method
    """

    # 모든 인스턴스가 공유
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # instance method
    # self 객체의 고유한 속성값 사용
    def detail_info(self):
        print("Current id {}".format(id(self)))
        print("Car detail info : {} {}".format(
            self._details.get('horsepower'), self._details.get('price')))

    def get_price(self):
        return 'Before carprice -> company : {} , price {}'.format(self._company, self._details['price'])

    def get_price_calc(self):
        return 'After carprice -> company : {} , price {}'.format(self._company, self._details['price']*Car.price_per_raise)

    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Bigger than 1")
            return
        else:
            cls.price_per_raise = per
            print("Succeed! price has changed")

    # Static method  애매하네....
    @staticmethod
    def is_bmw(car_inst):
        if car_inst._company == 'BMW':
            print("OK this car is BMW")
        else:
            print("SOrry this car is  {} ".format(car_inst._company))


car1 = Car('Ferrari', {'color': 'white1', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 500, 'price': 5000})
car3 = Car('Benz', {'color': 'Red', 'horsepower': 1000, 'price': 3000})

# 전체정보
car1.detail_info()
car2.detail_info()

# 가격정보
print(car1._details.get('price'))   # 직접접근하는건 좋지않어..

# 인상전
print(car1.get_price())
print(car2.get_price())

# 가격인상해볼까
Car.price_per_raise = 1.4

# 인상 후
print(car1.get_price_calc())
print(car2.get_price_calc())

# 가격인하 클래스메소드
Car.raise_price(1.2)


print(car1.get_price_calc())
print(car2.get_price_calc())

# 스태틱 사용
# 인스턴스로 호출
car1.is_bmw(car2)

# 클래스로 호출
Car.is_bmw(car1)
