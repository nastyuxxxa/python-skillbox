class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self.__coordinates = coordinates

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if not isinstance(speed, int):
            raise TypeError("Скорость должна быть целым числом")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        self.__speed = speed

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if not isinstance(brand, str):
            raise TypeError("Название бренда должно быть строкой")
        self.__brand = brand

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError("Год должен быть целым числом")
        if year <= 0:
            raise ValueError("Год должен быть положительным числом")
        self.__year = year

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not isinstance(number, str):
            raise TypeError("Номера должны быть строкой")
        self.__number = number

    def __str__(self):
        return str(
            f"Транспорт - Координаты: {self.coordinates}, Скорость: {self.speed}, Бренд: {self.brand}, Год: {self.year},Номер: {self.number}")

    def isInArea(self, pos_x, pos_y, length, width):
        x, y = self.coordinates[0], self.coordinates[1]
        return pos_x <= x <= pos_x + length and pos_y <= y <= pos_y + width


class Passenger:
    def __init__(self, passengers_capacity, number_of_passengers):
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if not isinstance(passengers_capacity, int):
            raise TypeError("Вместимость пассажиров должна быть целым числом")
        if passengers_capacity < 0:
            raise ValueError("Вмесимость пассажиров не может быть отрицательной")
        self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if not isinstance(number_of_passengers, int):
            raise TypeError("Кол-во пассажиров должно быть целым числом")
        if number_of_passengers < 0:
            raise ValueError("Кол-во пассажиров не может быть отрицательным")
        self.__number_of_passengers = number_of_passengers


class Cargo:
    def __init__(self, carrying):
        self.carrying = carrying

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if not isinstance(carrying, int):
            raise TypeError("Количество груза для судна должно быть целым числом")
        if carrying < 0:
            raise ValueError("Судно должно везти неотрицательное количество груза")
        self.__carrying = carrying


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("Высота должна быть целым числом")
        if height < 0:
            raise ValueError("Высота не может быть отрицательной")
        self.__height = height

    def __str__(self):
        return super().__str__() + f", Высота: {self.height}"


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.port = port

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        if not isinstance(port, str):
            raise TypeError("Название порта должно быть строкой")
        self.__port = port

    def __str__(self):
        return super().__str__() + f", Порт: {self.port}"


class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, carrying):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Cargo.__init__(self, carrying)


class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)


class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        Cargo.__init__(self, carrying)


class Airplane(Plane):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number, height)


class PassengerPlane(Plane, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, height, passengers_capacity, number_of_passengers):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class CargoPlane(Plane, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, height, carrying):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Cargo.__init__(self, carrying)


# Не разобралась как реализовать, может быть здесь возникает "проблема алмаза" из-за множественного наследования
class Seaplane(Plane, Ship):
    pass

#При такой реализации возникает ошибка
# class Seaplane(Plane, Ship):
#     def __init__(self, coordinates, speed, brand, year, number, height, port):
#         Plane.__init__(self, coordinates, speed, brand, year, number, height)
#         Ship.__init__(self, coordinates, speed, brand, year, number, port)
