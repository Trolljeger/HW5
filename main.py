'''
Создать класс с полями, в котором реализовать инициализатор и метод обработки данных.
Спроектировать иерархию классов от изначально написаного класса, используя наследование.
Дописать как минимум одно уникальное поле для каждого подкласса.
В классах-наследниках реализовать метод обработки данных.

Класс и его поля: Станок - производительность (изделий в час), стоимость станка, средняя цена детали

Метод 1: количество деталей для окупаемости
Иерархия: фрезерный станок, станок с ЧПУ
Метод 2: время окупаемости станка при фиксированной цене детали

Перегрузите оператор сложения add, который будет складывать производительность двух станков
'''

import math

class BaseMachine:
    '''
    Базовый класс для создания объекта типа станок
    '''

    def __init__(self, productivity, machine_price, detail_price):
        '''
        Конструктор объекта типа BaseMachine
        :param productivity: производительность станка (изделий в час), int
        :param machine_price: стоимость станка, float
        :param detail_price: средняя цена детали, float
        '''

        self.prod = productivity
        self.m_price = machine_price
        self.d_price = detail_price

    @property
    def prod(self):
        return self._prod

    @prod.setter
    def prod(self, productivity):
        if not isinstance(productivity, int):
            raise TypeError('Производительность станка должна быть типа int')
        if productivity < 0. :
            raise ValueError('Производительность станка должна быть положительной')

        self._prod = productivity

    @property
    def m_price(self):
        return self._m_price

    @m_price.setter
    def m_price(self, machine_price):
        if not isinstance(machine_price, float):
            raise TypeError('Стоимость станка должна быть типа float')
        if machine_price < 0. :
            raise ValueError('Стоимость станка должна быть положительной')

        self._m_price = machine_price

    @property
    def d_price(self):
        return self._d_price

    @d_price.setter
    def d_price(self, detail_price):
        if not isinstance(detail_price, float):
            raise TypeError('Стоимость детали должна быть типа float')
        if detail_price < 0. :
            raise ValueError('Стоимость детали должна быть положительной')

        self._d_price = detail_price


    def __add__(self, other):
        '''
        Функция сложения производительности двух станков
        :param other: объект типа станок
        :return: новый объект со средней стоимостью и суммарной производительностью
        '''
        if isinstance(other, self.__class__):
            return self.__class__(self.prod + other.prod, (self.m_price + other.m_price)/2., self.d_price)
        else:
            raise TypeError(f'Не могу объединить производительность станков {self.__class__} и {type(other)}')


    def __str__(self):
        '''
        Вывод параметров объекта в текстовом формате
        :return: строка описания
        '''

        return f'===================================================\n' \
               f'Объект типа {type(self)}: \n' \
               f'Производительность ==>> {self.prod} изделий в час\n' \
               f'Стоимость станка ==>> {self.m_price} \n' \
               f'Средняя стоимость детали ==>> {self.d_price} \n'


    def calc_payback_details(self):
        '''
        Функция возвращает число деталей для самоокупаемости
        :return: число деталей для самоокупаемости
        '''

        payback_num = 0

        try:
            payback_num = math.ceil(self.m_price/self.d_price)
        except ZeroDivisionError as ex:
            print('calc_payback_details:: Установлена нулевая стоимость детали.')
            raise ex

        return payback_num


    def calc_payback_time(self):

        '''
        Функция вычисления времени окупаемости станка
        :return: время окупаемости
        '''

        # Вычисляем количество деталей
        pb_num = self.calc_payback_details()

        pb_time = 0
        try:
            pb_time = math.ceil(pb_num/self.prod)
        except ZeroDivisionError as ex:
            print('calc_payback_time:: Установлена нулевая производительность.')
            raise ex

        return pb_time


class MillingMachine(BaseMachine):
    '''
    Класс Фрезерный станок
    '''
    def __init__(self, productivity, machine_price, detail_price, type = 'MillingMachine'):
        '''
        Конструктор объекта типа MillingMachine
        :param productivity: производительность станка (изделий в час), int
        :param machine_price: стоимость станка, float
        :param detail_price: средняя цена детали, float
        :param type: Тип станка, str
        '''
        super().__init__(productivity, machine_price, detail_price)
        self.m_type = type


    @property
    def m_type(self):
        return self._m_type

    @m_type.setter
    def m_type(self, type):
        if not isinstance(type, str):
            raise TypeError('Тип станка должен быть задан типом str')

        self._m_type = type

    def __add__(self, other):
        '''
        Функция сложения производительности двух станков
        :param other: объект типа станок
        :return: новый объект со средней стоимостью и суммарной производительностью
        '''
        if isinstance(other, self.__class__):
            return self.__class__(self.prod + other.prod,
                                  (self.m_price + other.m_price)/2.,
                                  self.d_price,
                                  self.m_type + '+' + other.m_type)
        else:
            raise TypeError(f'Не могу объединить производительность станков {self.__class__} и {type(other)}')


    def __str__(self):
        '''
        Вывод параметров объекта в текстовом формате
        :return: строка описания
        '''
        return  super().__str__() + f'Тип станка ==>> {self.m_type}\n'


class CncMachine(MillingMachine):
    '''
    Класс Станок с ЧПУ
    '''

    def __init__(self, productivity, machine_price, detail_price, type, acceleration = 1):
        '''
        Конструктор объекта типа CncMachine
        :param productivity: производительность станка (изделий в час), int
        :param machine_price: стоимость станка, float
        :param detail_price: средняя цена детали, float
        :param type: Тип станка, str
        :param acceleration: Коэффициент ускорения производительности, int
        '''
        super().__init__(productivity, machine_price, detail_price, type)
        self.accel = acceleration
        self.prod = self.prod * self.accel

    @property
    def accel(self):
        return self._accel

    @accel.setter
    def accel(self, acceleration):
        if not isinstance(acceleration, int):
            raise TypeError('Ускорение производительности станка должна быть типа int')
        if acceleration < 1. :
            raise ValueError('Ускорение производительности станка должно быть больше 1')

        self._accel = acceleration

    def __add__(self, other):
        '''
        Функция сложения производительности двух станков
        :param other: объект типа станок
        :return: новый объект со средней стоимостью и суммарной производительностью
        '''
        if isinstance(other, self.__class__):
            return self.__class__(self.prod + other.prod,
                                  (self.m_price + other.m_price) / 2.,
                                  self.d_price,
                                  self.m_type + '+' + other.m_type,
                                  (self.accel + other.accel) // 2)
        else:
            raise TypeError(f'Не могу объединить производительность станков {self.__class__} и {type(other)}')

    def __str__(self):
        '''
        Вывод параметров объекта в текстовом формате
        :return: строка описания
        '''
        return super().__str__() + f'Ускорение производительности ==>> {self.accel}\n'


#==============================================================================
#       Проверка базового класса BaseMachine
#==============================================================================
bm = BaseMachine(100, 10000., 5.)
print(bm)

payback_num = bm.calc_payback_details()
print(f'Для окупаемости станка необходимо произвести {payback_num} деталей')

pb_time = bm.calc_payback_time()
print(f'Для окупаемости станка необходимо {pb_time} часов\n')


#==============================================================================
#       Проверка класса MillingMachine
#==============================================================================
mm = MillingMachine(100, 20001., 5.2)
print(mm)
payback_num = mm.calc_payback_details()
print(f'Для окупаемости станка необходимо произвести {payback_num} деталей')

pb_time = mm.calc_payback_time()
print(f'Для окупаемости станка необходимо {pb_time} часов\n')


#==============================================================================
#       Проверка класса CncMachine
#==============================================================================
cm = CncMachine(100, 20001., 5.2, 'CncMachine', 2)
print(cm)
payback_num = cm.calc_payback_details()
print(f'Для окупаемости станка необходимо произвести {payback_num} деталей')

pb_time = cm.calc_payback_time()
print(f'Для окупаемости станка необходимо {pb_time} часов\n')


#==============================================================================
#       Проверка сложения производительности
#==============================================================================

bm1 = BaseMachine(100, 10000., 5.)
bm2 = BaseMachine(100, 5000., 5.)
summ_bm = bm1 + bm2
print(summ_bm)


mm1 = MillingMachine(100, 10000., 5.)
mm2 = MillingMachine(100, 5000., 5.)
summ_mm = mm1 + mm2
print(summ_mm)

cm1 = CncMachine(100, 10000., 5., 'CNC_100', 1)
cm2 = CncMachine(100, 5000., 5., 'CNC_200', 2)
summ_cm = cm1 + cm2
print(summ_cm)

summ_rm = bm1 + cm2
print(summ_rm)



