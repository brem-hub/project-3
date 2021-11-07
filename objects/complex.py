import math
import random
from typing import TextIO
from objects.number import Number


class Complex(Number):
    """
    Класс описывающий комплексное число.
    """

    def __init__(self):
        self._real: float = 0
        self._complex: float = 0

    def input(self, ifstream: TextIO) -> bool:
        """
        Ввод числа из файла.

        :param ifstream: дескриптор файла, открытый на чтение
        :return: флаг сигнализирующий об успешном или не успешном чтении числа из файла.
        """

        line = ifstream.readline()
        line_split = line.split()

        if len(line_split) != 2:
            print(f"could not read correct complex number from input file: {line}")
            return False

        try:
            self._real = float(line_split[0])
            self._complex = float(line_split[1])
            return True
        except ValueError as exc:
            print(f"Could not parse line `{line}` to complex number. Full error message: {exc}")
        except Exception as exc:
            print(f"Unexpected exception occurred during parsing complex number. Full error message: {exc}")

        return False

    def cast_to_float(self) -> float:
        """
        Получить float представление числа.

        :return: float представление числа
        """
        return math.sqrt(self._real * self._real + self._complex * self._complex)

    def random(self) -> None:
        """
        Случайное заполнение числа.
        """
        self._real = random.uniform(-100, 100)
        self._complex = random.uniform(-100, 100)

    def __str__(self):
        return f'complex number: {self._real:0.5f} + {self._complex:0.5f}i; double representation: {self.cast_to_float():0.5f}'

    def __repr__(self):
        return f'{Number.TYPE.COMPLEX}\n' \
               f'{self._real} {self._complex}'

