import pytest
from calculadora import Calculadora

def test_multiplicacao_dois_numeros_positivos():
    assert Calculadora().multiplicar(2, 5) == 10

def test_multiplicacao_numero_positivo_negativo():
    assert Calculadora().multiplicar(5, -3) == -15

def test_multiplicacao_numero_negativo_positivo():
    assert Calculadora().multiplicar(-5, 2) == -10

def test_multiplicacao_dois_numeros_negativos():
    assert Calculadora().multiplicar(-4, -6) == 24

def test_multiplicacao_numero_com_zero():
    assert Calculadora().multiplicar(0, 5) == 0

def test_multiplicacao_zeros():
    assert Calculadora().multiplicar(0, 0) == 0

def test_multiplicacao_numeros_decimais_positivos():
    assert Calculadora().multiplicar(3.5, 2.5) == 8.75

def test_multiplicacao_numeros_decimais_negativos():
    assert Calculadora().multiplicar(-3.5, 2.5) == -8.75
