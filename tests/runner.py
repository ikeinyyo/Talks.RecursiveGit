def ok(method):
    print("{}... Ok".format(method))

def ko(method, expected, found):
    print("{}... Error - Expected '{}' but found '{}'".format(method, expected, found))

def run_test(tests):
    pass_test = 0
    for test in tests:
        expected = test['expected']
        try:
            value = test['test']()
        except Exception as e:
            value = e.__class__.__name__
        if value == expected:
            ok(test['method'])
            pass_test += 1
        else:
            ko(test['method'], expected, value)

    print("\nTotal pass tests: {}/{}".format(pass_test, len(tests)))
