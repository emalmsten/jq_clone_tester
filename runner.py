import os

from classes import Test
from config import VERBOSE
from generators import generate
from other import cols, colorize
from tests import MultiTest


def run_all(all_tests):
    print(colorize("Started", cols.BLUE))
    print()
    for name, tests in all_tests.items():
        run_test_category(tests, name)


def remove_last_line_from_string(s):
    return s[:s.rfind('\n')]


def execute_test_case(cmd, data, name, i):
    jq_versions = ["jq", "jq-clone"]

    # if the data is a path to a json file, use type to get the contents, otherwise use echo
    get_data_command = "type" if ".json" in data else "echo"

    # comment the line above and uncomment this line for use on linux and mac (I think)
    # get_data_command = "cat" if ".json" in data else "echo"

    # get the results from running the command on the data with each jq version
    res_strs = map(lambda jq_version: os.popen(f"{get_data_command} {data} | {jq_version} \"{cmd}\"").read(),
                   jq_versions)

    # remove the last empty line from the results
    expected, actual = map(lambda res_str: remove_last_line_from_string(res_str), res_strs)

    passed = expected == actual
    # print(colorize("Passed", cols.GREEN)) if passed else print(colorize("Failed", cols.FAIL))

    start_str = f"    Test {colorize(name, cols.BOLD)}.."
    if not passed:
        print(" ", end='\r')
        print(start_str + colorize(f" Failed on test no {i}", cols.FAIL), end="")

    elif not VERBOSE:
        print(" ", end='\r')
        print(start_str + colorize(f" Passed: {i}", cols.GREEN), end=" ")

    if (not passed) or VERBOSE:
        col = cols.WARNING if not passed else cols.BLUE
        verbose_printing(cmd, expected, actual, col)

    return passed


def verbose_printing(cmd, expected, actual, color):
    indent = " " * 8
    expected_lines = expected.splitlines()
    actual_lines = actual.splitlines()

    if len(expected_lines) != 1 or len(actual_lines) != 1:
        expected = ''.join(list(map(lambda x: f"\n  {indent}{x}", expected_lines)))
        actual = ''.join(list(map(lambda x: f"\n  {indent}{x}", actual_lines)))

    print("")
    print(colorize(f"{indent}Command: ", color) + f"{cmd}")
    print(colorize(f"{indent}Expected: ", color) + f"{expected}")
    print(colorize(f"{indent}Actual: ", color) + f"{actual}")


def run_multi_test(test: MultiTest):
    """Generate values for the test and run it on them"""
    for i, generated in enumerate(generate(test)):
        if not execute_test_case(test.cmd(generated), test.data, test.name, i + 1):
            return False
    return True

def run_single_test(test: Test):
    """Generate values for the test and run it on them"""
    return execute_test_case(test.cmd, test.data, test.name, 1)

def run_test_category(category, name):
    print(f"Running tests for category {cols.BOLD}{name}{cols.ENDC}...")
    tests_failed = 0
    for test in category:
        result = run_multi_test(test) if isinstance(test, MultiTest) else run_single_test(test)
        if not result:
            tests_failed += 1
        print(" ")

    if tests_failed == 0:
        print(f"{cols.GREEN}All tests in category passed{cols.ENDC}")
    else:
        print(f"{cols.FAIL}Failed {tests_failed} tests{cols.ENDC}")
    print("")
    return tests_failed
