import datetime
import random
import string

from classes import Test
from config import GEN_TIMEOUT_MS
from other import colorize, cols

MIN_VALUE = -1000
MAX_VALUE = 1000
STD_STRING_LENGTH = 10


def generate(test: Test):
    values = []
    start_time = datetime.datetime.now()
    while len(values) < test.amount:
        value = test.generator()
        if test.condition(value):
            values.append(value)
        if (datetime.datetime.now() - start_time).total_seconds() > GEN_TIMEOUT_MS/1000:
            print(colorize(f"Only {len(values)} generated before timeout", cols.FAIL))
            break

    return values


# primitive generators
def gen_empty():
    return


def gen_ints(start=MIN_VALUE, end=MAX_VALUE):
    return lambda: random.randint(start, end)


def gen_floats(start=MIN_VALUE, end=MAX_VALUE, decimals=3):
    return lambda: round(random.uniform(start, end), decimals)


def gen_strings(length=STD_STRING_LENGTH):
    return lambda: ''.join(random.choice(string.ascii_letters) for _ in range(length))


# composite generators

def gen_array(generator, length=STD_STRING_LENGTH):
    return lambda: [generator() for _ in range(length)]


def gen_tuples(generators):
    return lambda: tuple([generators[i]() for i in range(len(generators))])
