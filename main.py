import sys
import time
from typing import TextIO

from container.container import Container
from utils.flag_handling import *

args = sys.argv


def is_flag_valid(flag: str, possible_flags: [str]) -> bool:
    """
    Проверить есть ли флаг в допустимых флагах.
    Метод больше предоставлен для сравнения с аналогичным методом на C(C++)

    :param flag: флаг, который нужно проверить
    :param possible_flags: доступные флаги
    :return: есть ли флаг среди доступных или нет
    """

    return flag in possible_flags


def find_flag(possible_flags: [str]) -> int:
    """
    Найти индекс любого флага из доступных среди argv

    :param possible_flags: доступные флаги
    :return: индекс первого доступного флага или -1, если такого нет
    """

    for possible_flag in possible_flags:
        try:
            pos = args.index(possible_flag)
            return pos
        except ValueError:
            continue
    return -1


def get_input_file() -> 'TextIO':
    """
    Обработать флаг `input`.

    :return: дескриптор файла, открытый на чтение
    :exception FlagException
    """
    input_flag_pos = find_flag(k_input_flags)

    if input_flag_pos == -1:
        raise FlagException(INPUT_FLAG_NOT_SPECIFIED_ERROR)

    if input_flag_pos + 1 >= len(args):
        raise FlagException(INPUT_FLAG_NOT_SET_ERROR)

    try:
        file = open(args[input_flag_pos + 1], 'r')
        return file
    except FileNotFoundError:
        raise FlagException(INPUT_FLAG_FILE_NOT_EXISTS_ERROR)


def get_output_file() -> 'TextIO':
    """
    Обработать флаг `output`.

    :return: дескриптор файла, открытый на запись
    :exception FlagException
    """

    output_flag_pos = find_flag(k_output_flags)

    if output_flag_pos == -1:
        raise FlagException(OUTPUT_FLAG_NOT_SPECIFIED_ERROR)

    if output_flag_pos + 1 >= len(args):
        raise FlagException(OUTPUT_FLAG_NOT_SET_ERROR)

    file = open(args[output_flag_pos + 1], 'w')
    return file


def get_random_size() -> int:
    """
    Обработать флаг `random`

    :return: количество случайно генерируемых элементов или -1, если флаг не указан.
    """

    random_size_flag_pos = find_flag(k_random_flags)

    if random_size_flag_pos == -1:
        return -1

    if random_size_flag_pos + 1 >= len(args):
        raise FlagException(RANDOM_SIZE_FLAG_NOT_SET_ERROR)

    try:
        random_size = int(args[random_size_flag_pos + 1])
    except ValueError:
        raise FlagException(RANDOM_SIZE_FLAG_INCORRECT_TYPE_ERROR)

    if random_size <= 0 or random_size > 10_000:
        raise FlagException(RANDOM_SIZE_FLAG_INCORRECT_ERROR)

    return random_size


# Если этот метод не сработает, то возможно необходимо удалить аннотацию типов.
# Данный вид аннотации был добавлен в Python 3.10: https://www.python.org/dev/peps/pep-0604/
def get_random_input_file() -> 'None | TextIO':
    """
    Обработать флаг `random-input`

    :return: дескриптор файла, открытый на запись или None
    """

    random_flag_pos = find_flag(k_random_input_flags)
    if random_flag_pos == -1:
        return None

    if random_flag_pos + 1 >= len(args):
        raise FlagException(RANDOM_INPUT_NOT_SPECIFIED_ERROR)

    file = open(args[random_flag_pos + 1], 'w')
    return file


def main():
    try:
        container = Container()

        if len(args) < 5:
            if len(args) == 2:
                if is_flag_valid(args[1], k_help_flags):
                    print(HELP_MESSAGE)
                    return
            raise FlagException(AGRC_EXCEPTION_MESSAGE)
        print("Initializing program")

        output_file = get_output_file()

        random_size = get_random_size()

        if random_size == -1:
            input_file = get_input_file()
            container.fill(input_file)
            input_file.close()
            print("Input parsed")
        else:
            random_input_file = get_random_input_file()
            container.random_fill(random_size, random_input_file)
            if random_input_file:
                random_input_file.close()
            print("Input generated")

        output_file.write(str(container))
        output_file.write("=======================\n\n")
        output_file.write(f"number of elements: {len(container)}\n")
        output_file.write(f"\n====| Straight Sort results | ====\n\n")

        print("Sorting elements")

        start_time = time.time()
        container.straight_sort()
        end_time = time.time()

        output_file.write(str(container))

        print("Exiting program")

        output_file.close()

        print(f"Elapsed: {end_time - start_time :0.9f} s")

    except FlagException as exc:
        print(f"{exc}\nException occurred during parsing flags, exiting.")
        return
    except ContainerException as exc:
        print(f"{exc}\nException occurred during program execution, exiting.")
        return
    except Exception as exc:
        print(f"Unexpected error occurred. Full error message: {exc}")


if __name__ == '__main__':
    main()
