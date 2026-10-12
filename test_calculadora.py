from calculadora import calcular_total, division, multiplicacion, resta, suma


def test_suma():
    assert suma(5, 3) == 8


def test_resta():
    assert resta(10, 4) == 6


def test_multiplicacion():
    assert multiplicacion(3, 5) == 15


def test_division():
    assert division(20, 5) == 4


def test_calcular_total():
    assert calcular_total(12, 3) == 36