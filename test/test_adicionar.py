import pytest
from calculadora import Calculadora


def test_soma_dois_numeros_positivos():
    assert Calculadora().adicionar(2, 5) == 7

def test_soma_numero_positivo_negativo():
    assert Calculadora().adicionar(5, -3) == 2

def test_soma_numero_negativo_positivo():
    assert Calculadora().adicionar(-5, 2) == -3

def test_soma_dois_numeros_negativos():
    assert Calculadora().adicionar(-4, -6) == -10

def test_soma_numero_com_zero():
    assert Calculadora().adicionar(0, 5) == 5

def test_soma_zeros():
    assert Calculadora().adicionar(0, 0) == 0

def test_soma_numeros_decimais_positivos():
    assert Calculadora().adicionar(12.000001, 3.500002) == 15.500003

def test_soma_numeros_decimais_negativos():
    assert Calculadora().adicionar(-3.000001, 3.500001) == 0.500000