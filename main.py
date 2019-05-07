from tests.tests import create_test
from tests.runner import run_test

if __name__ == "__main__":
    tests = create_test()
    run_test(tests)
