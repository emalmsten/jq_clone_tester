import datetime
import random
import string

from classes import MultiTest
from config import GEN_TIMEOUT_MS
from other import colorize, cols, timeout

MIN_VALUE = -1000
MAX_VALUE = 1000
STD_STRING_LENGTH = 10


def generate(test: MultiTest):
    """Generates values for a test"""
    values = []
    start_time = datetime.datetime.now()

    # generate values until the amount or timeout is reached
    while len(values) < test.amount:
        value = test.generator()
        if test.condition(value):
            values.append(value)
        if timeout(GEN_TIMEOUT_MS, start_time):
            print(colorize(f"Only {len(values)} values generated before timeout", cols.WARNING), end="  ")
            break

    return values


# primitive generators


def gen_int(start=MIN_VALUE, end=MAX_VALUE):
    return lambda: random.randint(start, end)


def gen_float(start=MIN_VALUE, end=MAX_VALUE, decimals=3):
    return lambda: round(random.uniform(start, end), decimals)


def gen_bool():
    return lambda: random.choice([True, False])


def gen_letter():
    return lambda: random.choice(string.ascii_letters)


# composite generators

def gen_string(length=STD_STRING_LENGTH):
    return lambda: ''.join([gen_letter()() for _ in range(length)])


def gen_array(generator, length=STD_STRING_LENGTH):
    return lambda: [generator() for _ in range(length)]


def gen_tuple(generators):
    return lambda: tuple([generators[i]() for i in range(len(generators))])
