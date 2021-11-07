k_help_flags = ['-h', '--help']

k_input_flags = ['-i', '--input']

k_output_flags = ['-o', '--output']

k_random_flags = ['-r', '--random']

k_random_input_flags = ['--random-input']


HELP_MESSAGE = "HSE UNIVERSITY, 2021-2022, Kulikov Bogdan, third project program.\n" \
               "Task: 11, Function: 10\n" \
               "\n" \
               "Usage: python main.py [OPTIONS]...\n" \
               "\n" \
               "OPTIONS:\n" \
               " -i, --input\t\t Specify input file\n" \
               " -o, --output\t\t Specify output file\n" \
               "\t\t\t\t if file does not exist - program will create one\n" \
               " -r, --random\t\t Generate random input. Range [1, 10000]\n" \
               " --random-input\t\t Create file with generated input\n" \
               "\n" \
               "\n" \
               "INPUT SPECIFICATION:\n" \
               "Input file starts with number of elements (int_32)\n" \
               "Elements consist of fields:\n" \
               "\t `element_type`: 0 - COMPLEX, 1 - FRACTION, 2 - POLAR\n" \
               "\t `element_description`:\n" \
               "\t\t COMPLEX: A pair of float numbers - real and imaginary parts.\n" \
               "\t\t\t  example: `10.1 12.0` -> complex: (real=10.1, imaginary=12.0)\n" \
               "\t\t FRACTION: A pair of int numbers - numerator and denominator.\n" \
               "\t\t\t  example: `1 2` -> fraction: 1/2\n" \
               "\t\t POLAR: A float number - angle and a pair of int numbers - coordinates.\n" \
               "\t\t\t  example: `10.1 3 4` -> polar: (angle=10.1, coords=(x=3,y=4))\n" \
               "See example at /tests/input/example.txt"

TRY_HELP_MESSAGE = "Try 'program --help(-h)' for more information."

AGRC_EXCEPTION_MESSAGE = f"Incorrect program input.\n{TRY_HELP_MESSAGE}"

RANDOM_SIZE_FLAG_NOT_SET_ERROR = f"Random size flag is empty.\n{TRY_HELP_MESSAGE}"

RANDOM_SIZE_FLAG_INCORRECT_TYPE_ERROR = "Random size must be integer with base 10."

RANDOM_SIZE_FLAG_INCORRECT_ERROR = "Number of random elements cannot be negative or 0 and must be less 10.000."

INPUT_FLAG_NOT_SPECIFIED_ERROR = f"Input flag was not specified.\n{TRY_HELP_MESSAGE}"

INPUT_FLAG_NOT_SET_ERROR = f"Input flag is empty.\n{TRY_HELP_MESSAGE}"

INPUT_FLAG_FILE_NOT_EXISTS_ERROR = "Input file does not exists.\n"

OUTPUT_FLAG_NOT_SPECIFIED_ERROR = f"Output flag was not specified.\n{TRY_HELP_MESSAGE}"

OUTPUT_FLAG_NOT_SET_ERROR = f"Output flag is empty.\n{TRY_HELP_MESSAGE}"

OUTPUT_FLAG_FILE_NOT_EXISTS_ERROR = "Input file does not exists.\n"

RANDOM_INPUT_NOT_SPECIFIED_ERROR = f"Random input file was not specified.\n{TRY_HELP_MESSAGE}"


class FlagException(Exception):
    """
    Исключение описывающее ошибку с обработкой флагов.
    """
    pass


class ContainerException(Exception):
    """
    Исключение описывающее ошибку с работой программы.
    """
    pass
