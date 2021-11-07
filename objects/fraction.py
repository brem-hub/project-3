import random
from typing import TextIO

from objects.number import Number


class Fraction(Number):
    """
    Класс описывающий дробное число
    """

    def __init__(self):
        self._numerator: int = 0
        self._denominator: int = 0

    def input(self, ifstream: TextIO) -> bool:
        """
        Ввод числа из файла.

        :param ifstream: дескриптор файла, открытый на чтение
        :return: флаг сигнализирующий об успешном или не успешном чтении числа из файла.
        """

        line = ifstream.readline()
        line_split = line.split()

        if len(line_split) != 2:
            print(f"Could not read correct complex number from input file: {line}")
            return False

        try:
            self._numerator = int(line_split[0])
            self._denominator = int(line_split[1])
        except ValueError as exc:
            print(f"Could not parse `{line}` to fraction number. Full error message: {exc}")
            return False
        except Exception as exc:
            print(f"Unexpected exception occurred during parsing fraction number. Full error message: {exc}")
            return False

        if self._denominator == 0:
            print(f"Denominator cannot be 0, input for fraction is incorrect")
            return False

        return True

    def random(self) -> None:
        """
        Случайное заполнение числа.
        """

        self._numerator = random.randint(-100,  100)
        while self._denominator == 0:
            self._denominator = random.randint(-100, 100)

    def cast_to_float(self) -> float:
        """
        Получить float представление числа.

        :return: float представление числа
        """

        return self._numerator / self._denominator

    def __str__(self):
        return f'fraction {self._numerator}/{self._denominator}; float representation: {self.cast_to_float():0.5f}'

    def __repr__(self):
        return f'{Number.TYPE.FRACTION}\n' \
               f'{self._numerator} {self._denominator}'
