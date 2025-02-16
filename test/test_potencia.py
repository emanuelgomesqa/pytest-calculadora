import pytest
from calculadora import Calculadora

def test_potencia_dois_numeros_positivos():
    assert Calculadora().potencia(2, 3) == 8

def test_potencia_numero_positivo_zero():
    assert Calculadora().potencia(5, 0) == 1

def test_potencia_numero_zero_positivo():
    assert Calculadora().potencia(0, 5) == 0

def test_potencia_numero_negativo_positivo():
    assert Calculadora().potencia(-2, 3) == -8

def test_potencia_numero_positivo_negativo():
    assert Calculadora().potencia(2, -3) == 0.125

def test_potencia_dois_numeros_negativos():
    assert Calculadora().potencia(-2, -3) == -0.125

def test_potencia_numero_com_zero():
    assert Calculadora().potencia(0, 0) == 1

def test_potencia_numeros_decimais():
    assert Calculadora().potencia(2.5, 2) == 6.25
