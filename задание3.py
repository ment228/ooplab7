import random
class Flower:
    def __init__(self, stem_length, freshness):
        self.__stem_length=stem_length
        self.__freshness=freshness
    @property
    def stem_length(self):
        return self.__stem_length
    @stem_length.setter
    def stem_length(self, value):
        if not isinstance(value, int):
            print('Длина стебля должна быть числом')
        elif value < 5:
            print('Длина стебля должна быть минимум 5')
        elif value > 20:
            print('Длина стебля должна быть максимум 20')
        else:
            self.__stem_length=value
    @property
    def freshness(self):
        return self.__freshness
    @freshness.setter
    def freshness(self, value):
        if not isinstance(value, int):
            print('Уровень свежести должен быть числом')
        elif value<1:
            print('Уровень свежести должен быть минимум 1')
        elif value>10:
            print('Уровень свежести должен быть максимум 10')
        else:
            self.__freshness=value
f=[]
for i in range(5):
    f.append(Flower(int(random.uniform(5, 20)), int(random.uniform(1, 10))))
    print(f'Цветок {i+1}: длина стебля {f[i].stem_length}, уровень свежести {f[i].freshness}')
result=sorted(f, key=lambda x: x.freshness)
print('\nОтсортированный букет:')
for i in range(5):
    print(f'Цветок {i+1}-уровень свежести {result[i].freshness}')
start=int(input('Введите начальное значение диапазона: '))
end=int(input('Введите конечное значение диапазона: '))
for i in range(5):
    if start<=f[i].stem_length<=end:
        print(f'Цветок {i+1}-длина стебля {f[i].stem_length}')