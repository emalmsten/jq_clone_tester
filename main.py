from runner import *
from tests import *

all_tests = {}

# concatenate all the tests wanted
all_tests.update(identity_tests)
all_tests.update(object_index_tests)
all_tests.update(array_tests)

if __name__ == '__main__':
    run_all(all_tests)
