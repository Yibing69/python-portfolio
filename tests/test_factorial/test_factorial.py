from factorial.factorial import factorial
# 5! = 5 * 4 * 3 * 2 * 1 = 120

def test_factorial():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
