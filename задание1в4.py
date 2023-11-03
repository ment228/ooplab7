'''Класс Bus: Фамилия и инициалы водителя, Номер автобуса, Номер
маршрута, Марка, Год начала эксплуатации, Пробег

свойства: Год начала эксплуатации, Пробег
'''
class Bus:#новый класс Bus
    def __init__(self, driver_initials, bus_number, marsh_number, brand, start_year, probeg):
#конструктор с параметрами Фамилия и инициалы водителя, Номер автобуса, Номер
#маршрута, Марка, Год начала эксплуатации, Пробег
        self._driver_initials = driver_initials
        self._bus_number = bus_number
        self._marsh_number = marsh_number
        self._brand = brand
        self._start_year = start_year
        self._probeg = probeg#инициализируем параметры
    @property
    def driver_initials(self):
        return self._driver_initials
    @property
    def bus_number(self):
        return self._bus_number
    @property
    def marsh_number(self):
        return self._marsh_number
    @property
    def brand(self):
        return self._brand
    @property
    def start_year(self):
        return self._start_year
    @property
    def probeg(self):
        return self._probeg#объявление методов каждый из кторых возвращает значения переменных и каждая из которых является декоратором
bus = Bus("Мерседенскинс А.В.", "ru5038i3", "274", "Maz", 1999, 7034)
print("класс Bus")
print("инициалы и фамилия водителя:", bus.driver_initials)
print("номер автобуса:", bus.bus_number)
print("номер маршрута:", bus.marsh_number)
print("марка:", bus.brand)
print("год начала эксплуатации:", bus.start_year)
print("пробег:", bus.probeg)#вывод данных