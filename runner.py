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
    jq = ["jq", "jq-clone"]
    get_data_command = "type" if ".json" in data else "echo"

    res_strs = map(lambda jq_version: os.popen(f"{get_data_command} {data} | {jq_version} \"{cmd}\"").read(), jq)

    expected, actual = map(lambda res_str: remove_last_line_from_string(res_str), res_strs)

    passed = expected == actual
    if not passed:
        print(colorize("Failed", cols.FAIL))
        print(f"{cols.WARNING}        Command: {cols.ENDC}{cmd}")
        print(f"{cols.WARNING}        Expected: {cols.ENDC}{expected}")
        print(f"{cols.WARNING}        Actual: {cols.ENDC}{actual}")
        return False

    print(colorize("Passed", cols.GREEN))
    if VERBOSE:
        print(f"{cols.BLUE}          Command: {cols.ENDC}{cmd}")
        print(f"{cols.BLUE}          Expected: {cols.ENDC}{expected}")
        print(f"{cols.BLUE}          Actual: {cols.ENDC}{actual}")

    return True


def run_tests(test: Test):
    print(f"    Test {colorize(test.name, cols.BOLD)}..", end=" ")
    for generated in (generate(test)):
        if not run_test(test.cmd(generated), test.data):
            return False

    return True


def run_test_category(category, name):
    print(f"Running tests for {cols.BOLD}{name}{cols.ENDC}...")
    tests_failed = 0
    for test in category:
        result = run_tests(test)
        if not result:
            tests_failed += 1

    if tests_failed == 0:
        print(f"{cols.GREEN}Tests in category passed{cols.ENDC}")
    else:
        print(f"{cols.FAIL}Failed {tests_failed} tests{cols.ENDC}")
    print("")
    return tests_failed
