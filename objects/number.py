from __future__ import annotations

import abc
from typing import TextIO
from enum import IntEnum, unique

import objects
from utils.utils import empty_object, try_parse


class Number:
    """
        Абстрактный класс, описывающий интерфейс числа.
    """

    @unique
    class TYPE(IntEnum):
        """
        Перечисление видов чисел. Необходимо для сериализации.
        """
        COMPLEX = 0
        FRACTION = 1
        POLAR = 2

    @abc.abstractmethod
    def input(self, ifstream: TextIO) -> bool:
        """
        Ввод числа из файла.

        :param ifstream: дескриптор файла, открытый на чтение
        :return: флаг сигнализирующий об успешном или не успешном чтении числа из файла.
        """

    @abc.abstractmethod
    def random(self) -> None:
        """
        Случайное заполнение числа.
        """

    @abc.abstractmethod
    def cast_to_float(self) -> float:
        """
        Получить float представление числа.

        :return: float представление числа
        """

    def __str__(self):
        """
        Воспользуемся встроенными функциями в Python3 для получения строки по объекту.
        Т.к. в Python3 все классы наследуются от `object`, то мы можем переопределять методы
         класса object, такие как __str__ и __repr__.
        Тогда встроенная функция str() будет получать human-readable формат числа,
         а функция repr() - формат для генератора.
        В базовом классе `number` переопределение не несёт никакого смысла, кроме примера.
        """
        return "number"

    def __repr__(self):
        return "0"


# Если этот метод не сработает, то возможно необходимо удалить аннотацию типов.
# Данный вид аннотации был добавлен в Python 3.10: https://www.python.org/dev/peps/pep-0604/
def read_number(ifstream: TextIO) -> 'None | Number':
    """
    Статический метод для десериализации числа из файла.

    :param ifstream: дескриптор файла, открытый на чтение
    :return: десериализованное число - наследник класса `number` или None, если произошла ошибка.
    """

    number_type = try_parse(ifstream.readline(), int)

    if number_type == empty_object:
        print("Could not parse number type")
        return None

    number_type_ctor = try_parse(number_type, Number.TYPE)

    if number_type_ctor == empty_object:
        print(f"Could not parse type of number: {number_type}")
        return None

    # Пользуемся словарем с типами чисел по перечислению
    number = objects.number_types[number_type_ctor]()

    res = number.input(ifstream)
    if res:
        return number

    return None
