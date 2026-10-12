from calculadora import division, multiplicacion, resta, suma


def test_suma():
    assert suma(5, 3) == 8


def test_resta():
    assert resta(10, 4) == 6


def test_multiplicacion():
    assert multiplicacion(3, 5) == 15


def test_division():
    assert division(20, 5) == 4