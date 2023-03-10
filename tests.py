from generators import *
from classes import MultiTest, Test
import os.path

# the path to the json files
data_files_path = "data_files"

# the jq command to be run
index_cmd = lambda x: f".[{x}]"
slice_cmd = lambda xs: f".[{xs[0]}:{xs[1]}]"

# the json to run the command on (in this case just an array)
test_array = "[1, 2, 3, 4, 5]"

array_tests = {
    # the test category
    "Array Index Tests": [
        # instances of tests
        MultiTest("Floats", index_cmd, test_array, generator=gen_float(-10, 10)),
        MultiTest("Ints", index_cmd, test_array, generator=gen_int(-10, 10), condition=lambda x: x % 2 == 0),
    ],
    "Array Slice": [
        MultiTest("Ints", slice_cmd, test_array, generator=gen_array(gen_int(-10, 10), length=2)),
    ],
}

# a path to a json file
example_file = os.path.join(data_files_path, "example.json")

identity_tests = {
    "Identity": [
        Test("Simple", cmd=".", data="1"),
        Test("Example File", cmd=".", data=example_file),
    ]
}

obj_idx_cmd = lambda x: f".{x}"
test_obj = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'

object_index_tests = {
    "Object Index": [
        MultiTest("Simple", obj_idx_cmd, test_obj, generator=gen_letter(), condition=lambda x: x in "abcde"),
    ]
}


