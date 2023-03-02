import os

from config import VERBOSE
from generators import generate
from other import cols, colorize
from tests import Test


def run_all(all_tests):
    print(colorize("Started", cols.BLUE))
    print()
    for name, tests in all_tests.items():
        run_test_category(tests, name)


def remove_last_line_from_string(s):
    return s[:s.rfind('\n')]


def run_test(cmd, data):
    jq_versions = ["jq", "jq-clone"]

    # if the data is a path to a json file, use type to get the contents, otherwise use echo
    get_data_command = "type" if ".json" in data else "echo"

    # get the results from running the command on the data with each jq version
    res_strs = map(lambda jq_version: os.popen(f"{get_data_command} {data} | {jq_version} \"{cmd}\"").read(), jq_versions)

    # remove the last line from the results
    expected, actual = map(lambda res_str: remove_last_line_from_string(res_str), res_strs)

    passed = expected == actual
    print(colorize("Passed", cols.GREEN)) if passed else print(colorize("Failed", cols.FAIL))

    if not passed or VERBOSE:
        col = cols.WARNING if not passed else cols.BLUE
        print(f"{col}        Command: {cols.ENDC}{cmd}")
        print(f"{col}        Expected: {cols.ENDC}{expected}")
        print(f"{col}        Actual: {cols.ENDC}{actual}")

    return passed


def run_tests(test: Test):
    """Generate values for the test and run it on them"""

    print(f"    Test {colorize(test.name, cols.BOLD)}..", end=" ")
    for generated in (generate(test)):
        if not run_test(test.cmd(generated), test.data):
            return False

    return True


def run_test_category(category, name):
    print(f"Running tests for category {cols.BOLD}{name}{cols.ENDC}...")
    tests_failed = 0
    for test in category:
        result = run_tests(test)
        if not result:
            tests_failed += 1

    if tests_failed == 0:
        print(f"{cols.GREEN}All tests in category passed{cols.ENDC}")
    else:
        print(f"{cols.FAIL}Failed {tests_failed} tests{cols.ENDC}")
    print("")
    return tests_failed
