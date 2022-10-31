#illustration of assertion error
n = -5
try:
    assert n > 5
    print("number is positive")
except AssertionError:
    print("Assertion error exception raised")
