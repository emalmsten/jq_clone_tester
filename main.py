from runner import *
from tests import *
import os

all_tests = {}

# concatenate all the tests wanted
all_tests.update(identity_tests)
all_tests.update(object_index_tests)
all_tests.update(array_tests)

# To automatically run stack install before testing uncomment the following line, and change the path to the one
#   containing your fp project (from the root of your home directory). Then uncomment line 18 in this file
# fp_path = os.path.join(os.environ["HOMEPATH"], YOUR_FP_DIRECTORY_FROM_HOME)
# https://www.geeksforgeeks.org/python-os-path-join-method/

if __name__ == '__main__':
    # os.system(f"cd {fp_path} && stack install")
    run_all(all_tests)
