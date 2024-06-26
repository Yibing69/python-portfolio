from factorial.factorial import factorial


# 4 * (3 * (2 * (1)))

def test_factorial():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
