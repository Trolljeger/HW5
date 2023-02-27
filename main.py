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

        if(int != type(productivity) or float != type(machine_price) or float != type(detail_price)):
            raise TypeError(
                f'Неверный тип входных данных. \n'
            )

        self.prod = productivity
        self.m_price = machine_price
        self.d_price = detail_price

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
    def __init__(self, productivity, machine_price, detail_price, type):
        '''
        Конструктор объекта типа MillingMachine
        :param productivity: производительность станка (изделий в час), int
        :param machine_price: стоимость станка, float
        :param detail_price: средняя цена детали, float
        :param type: Тип станка, str
        '''
        super().__init__(productivity, machine_price, detail_price)
        self.m_type = type


    def __str__(self):
        '''
        Вывод параметров объекта в текстовом формате
        :return: строка описания
        '''
        return  super().__str__() + f'Тип станка == >> {self.m_type}\n'


class CncMachine(MillingMachine):
    '''
    Класс Станок с ЧПУ
    '''

    def __init__(self, productivity, machine_price, detail_price, type, acceleration):
        '''
        Конструктор объекта типа CncMachine
        :param productivity: производительность станка (изделий в час), int
        :param machine_price: стоимость станка, float
        :param detail_price: средняя цена детали, float
        :param type: Тип станка, str
        :param acceleration: Коэффициент ускорения производительности
        '''
        super().__init__(productivity, machine_price, detail_price, type)
        self.accel = acceleration

    def __str__(self):
        '''
        Вывод параметров объекта в текстовом формате
        :return: строка описания
        '''
        return super().__str__() + f'Ускорение производительности == >> {self.accel}\n'


    def calc_payback_time(self):
        '''
        Функция вычисления времени окупаемости станка с учетом ускорения
        :return: время окупаемости
        '''

        payback_time = super().calc_payback_time()
        try:
            payback_time = math.ceil(payback_time/self.accel)
        except ZeroDivisionError as ex:
            print('calc_payback_time:: Установлено нулевое ускорение производительности.')
            raise ex

        return payback_time




#==============================================================================
bm = BaseMachine(100, 10000., 5.)
print(bm)

payback_num = bm.calc_payback_details()
print(f'Для окупаемости станка необходимо произвести {payback_num} деталей')

pb_time = bm.calc_payback_time()
print(f'Для окупаемости станка необходимо {pb_time} часов\n')

#==============================================================================
mm = MillingMachine(100, 20001., 5.2, 'MillingMachine')
print(mm)
payback_num = mm.calc_payback_details()
print(f'Для окупаемости станка необходимо произвести {payback_num} деталей')

pb_time = mm.calc_payback_time()
print(f'Для окупаемости станка необходимо {pb_time} часов\n')

#==============================================================================
cm = CncMachine(100, 20001., 5.2, 'CncMachine', 2)
print(cm)
payback_num = cm.calc_payback_details()
print(f'Для окупаемости станка необходимо произвести {payback_num} деталей')

pb_time = cm.calc_payback_time()
print(f'Для окупаемости станка необходимо {pb_time} часов\n')