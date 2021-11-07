import math
import random
from typing import TextIO

from objects.number import Number
from objects.point import Point


class Polar(Number):
    """
    Класс описывающий полярное число.
    """

    def __init__(self):
        self._angle: float = 0
        self._coords: Point = Point()

    def input(self, ifstream: TextIO) -> bool:
        """
        Ввод числа из файла.

        :param ifstream: дескриптор файла, открытый на чтение
        :return: флаг сигнализирующий об успешном или не успешном чтении числа из файла.
        """

        line = ifstream.readline()
        line_split = line.split()

        if len(line_split) != 3:
            print(f"Could not read correct polar number from input file: {line}")
            return False

        try:
            self._angle = float(line_split[0])
            self._coords = Point(int(line_split[1]), int(line_split[2]))
            return True
        except ValueError as exc:
            print(f"Could not parse `{line}` to polar number. Full error message: {exc}")
        except Exception as exc:
            print(f"Unexpected exception occurred during parsing polar number. Full error message: {exc}")

    def random(self) -> None:
        """
        Случайное заполнение числа.
        """

        self._angle = random.uniform(-100, 100)
        self._coords = Point(random.randint(-100, 100), random.randint(-100, 100))

    def cast_to_float(self) -> float:
        """
        Получить float представление числа.

        :return: float представление числа
        """

        return math.sqrt(math.pow(self._coords.x, 2) + math.pow(self._coords.y, 2))

    def __str__(self):
        return f'polar number: w={self._angle:0.5f}, coords=({self._coords.x}, {self._coords.y});' \
               f' float representation: {self.cast_to_float():0.5f}'

    def __repr__(self):
        return f'{Number.TYPE.POLAR}\n' \
               f'{self._angle} {self._coords.x} {self._coords.y}'

