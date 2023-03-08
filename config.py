# How much is printed
VERBOSE = False

# Maximum time for generating x tests
GEN_TIMEOUT_MS = 5000

# Amount of values to run for each multitest
STD_AMT_TESTS = 25

# If set to true, if both jq and jq-clone return an error, it's considered a passed test.
# It only works if your error message in jq-clone has the word "error" in it (this is NOT the default)
# This is useful for tests that are supposed to fail.
# Be aware(!!) that if you set this to true a faulty JSON file or jq command can cause a false positive
ERRORS_ARE_EQUAL = False
