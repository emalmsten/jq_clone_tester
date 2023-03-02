from generators import *
from classes import Test
import os.path


data_path = "data_files"

index_cmd = lambda x: f".[{x}]"
slice_cmd = lambda xs: f".[{xs[0]}:{xs[1]}]"

random_array = "[1, 2, 3, 4, 5]"

array_tests = {
    "Array Index Tests": [
        Test("ints", index_cmd, random_array, gen_ints(-10, 10)),
        Test("floats", index_cmd, random_array, gen_floats(-10, 10)),
    ],
    "Array Slice": [
        Test("Ints", slice_cmd, random_array, gen_array(gen_ints(-10, 10), 2)),
    ],
}

object_index_tests = {

}

example_file = os.path.join(data_path, "example.json")

identity_cmd = lambda _: "."

identity_tests = {
    "Identity": [
        Test("simple", identity_cmd, "1", gen_empty, amount=1),
        Test("meteorites", identity_cmd, example_file, gen_empty, amount=1),
    ]
}

all_tests = {}

all_tests.update(identity_tests)
all_tests.update(array_tests)

