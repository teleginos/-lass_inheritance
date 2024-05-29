class Car:
    price = 1000000

    def __init__(self, brand):
        self.brand = brand

    def horse_power(self):
        return 100

    def __str__(self):
        return f"Машина марки {self.brand}\nСоздана из класса {self.__class__.__name__} Стоимость: {self.price} рублей"


class Nissan(Car):
    price = 5000000

    def horse_power(self):
        return 200


class Kia(Car):
    price = 3500000

    def horse_power(self):
        return 150


if __name__ == '__main__':
    car = Car('Lada')
    print(car, end=' ')
    print(f"Мощность: {car.horse_power()} лошадиных сил")
    nissan = Nissan('Nissan')
    print(nissan, end=' ')
    print(f"Мощность: {nissan.horse_power()} лошадиных сил")
    kia = Kia('Kia')
    print(kia, end=' ')
    print(f"Мощность: {kia.horse_power()} лошадиных сил")
