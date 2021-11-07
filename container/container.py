import random
from typing import TextIO
from objects import number_types, Number
from objects.number import read_number
from utils.flag_handling import ContainerException
from utils.utils import try_parse, empty_object


class Container:
    """
    Класс, предоставляющий доступ к списку с возможностью сортировки.
    """

    def __init__(self):
        self._list: [Number] = []

    def fill(self, ifstream: TextIO) -> None:
        """
        Заполнить контейнер из файла.

        :param ifstream: дескриптор файла, открытый на чтение.
        """

        number_of_elements = try_parse(ifstream.readline(), int)

        if number_of_elements == empty_object:
            raise ContainerException(f"Could not read number of elements in the file.")

        if number_of_elements <= 0:
            raise ContainerException('Number of elements cannot be less or equal to 0')

        for i in range(number_of_elements):
            number = read_number(ifstream)
            if number is None:
                raise ContainerException()

            self._list.append(number)

    def random_fill(self, number_of_elements: int, ofstream: TextIO = None) -> None:
        """
        Заполнить файл случайными числами.
        :param number_of_elements: количество случайных чисел.
        :param ofstream: [optional] дескриптор файла, открытый на запись.
            В ofstream можно записать входные данные в формате входящих данных.
        :exception ContainerException
        """

        if number_of_elements <= 0:
            raise ContainerException("Random size cannot be <= 0")

        if ofstream is not None:
            ofstream.write(str(number_of_elements) + "\n")

        for i in range(number_of_elements):
            type = random.randint(0, 2)

            number = number_types[Number.TYPE(type)]()
            number.random()
            self._list.append(number)

            if ofstream is not None:
                data = repr(number)
                ofstream.write(data + "\n")

    def straight_sort(self) -> None:
        """
        Сортировка контейнера.
        """

        for i in range(len(self)):
            number = self._list[i]
            j = i
            while j > 0 and self._list[j - 1].cast_to_float() > number.cast_to_float():
                self._list[j] = self._list[j - 1]
                j -= 1
            self._list[j] = number

    # Пользуемся тем, что любой класс в Python - наследник `object`,
    #  сл-но можем переопределять базовые методы.
    def __str__(self):
        str_rep = ""
        for i in range(len(self._list)):
            str_rep += f"{i}) {self._list[i]}\n"
        return str_rep

    def __len__(self):
        return len(self._list)
