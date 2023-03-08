import os

from classes import Test
from config import *
from generators import generate
from other import cols, colorize
from tests import MultiTest
from subprocess import PIPE, Popen


def run_all(all_tests):
    print(colorize("Started", cols.BLUE))
    print()
    for name, tests in all_tests.items():
        run_test_category(tests, name)


def remove_last_line_from_string(s):
    return s[:s.rfind('\r\n')]


def run_in_command_line(get_data_command, cmd, data, jq_version):
    res = Popen(f"{get_data_command} {data} | {jq_version} \"{cmd}\"", shell=True, stdout=PIPE,
                stderr=PIPE).communicate()
    return list(map(lambda s: remove_last_line_from_string(s.decode("utf-8").lower()), res))


def execute_test_case(cmd, data, name, i):
    jq_versions = ["jq", "jq-clone"]

    # if the data is a path to a json file, use type to get the contents, otherwise use echo
    get_data_command = "type" if ".json" in data else "echo"

    # comment the line above and uncomment this line for use on linux and mac (I think)
    # get_data_command = "cat" if ".json" in data else "echo"

    # get the results from running the command on the data with each jq version
    expected, actual = map(lambda jq_version: run_in_command_line(get_data_command, cmd, data, jq_version), jq_versions)

    # expected[0] holds the result, and expected[1] holds the error message.
    # If there is no error, expected[1] is empty and vice versa
    if "error" in expected[1]:
        expected[0] = expected[1]

    expected = expected[0]
    actual = actual[0]

    result = "pass" if expected == actual else "fail"

    if ERRORS_ARE_EQUAL and ("error" in expected and "error" in actual):
        result = "error_pass"

    fail = result == "fail"

    start_str = f"    Test {colorize(name, cols.BOLD)}.."
    if fail:
        print(" ", end='\r')
        print(start_str + colorize(f" Failed on test no {i}", cols.FAIL), end="")

    elif not VERBOSE:
        print(" ", end='\r')
        print(start_str + colorize(f" Passed: {i}", cols.GREEN), end=" ")

    if fail or VERBOSE:
        col = cols.WARNING if fail else cols.BLUE
        verbose_printing(cmd, expected, actual, col)

    return result


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
    error_passes = 0
    for i, generated in enumerate(generate(test)):
        res = execute_test_case(test.cmd(generated), test.data, test.name, i + 1)
        if res == "fail":
            return False, error_passes
        elif res == "error_pass":
            error_passes += 1
    return True, error_passes


def run_single_test(test: Test):
    """Generate values for the test and run it on them"""
    res = execute_test_case(test.cmd, test.data, test.name, 1)
    return res, 1 if res == "error_pass" else 0


def run_test_category(category, name):
    print(f"Running tests for category {cols.BOLD}{name}{cols.ENDC}...")
    tests_failed = 0
    for test in category:
        result, error_passes = run_multi_test(test) if isinstance(test, MultiTest) else run_single_test(test)
        if result == "fail":
            tests_failed += 1
        elif error_passes > 0:
            print(f"{cols.WARNING}      {error_passes} tests in {test.name} passed due to errors in both jq and jq-clone{cols.ENDC}")
        print(" ")

    if tests_failed == 0:
        print(f"{cols.GREEN}All tests in category passed{cols.ENDC}")
    else:
        print(f"{cols.FAIL}Failed {tests_failed} tests{cols.ENDC}")
    print("")
    return tests_failed
