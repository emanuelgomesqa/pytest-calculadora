import pytest
from calculadora import Calculadora

def test_divisao_dois_numeros_positivos():
    assert Calculadora().dividir(10, 2) == 5

def test_divisao_numero_positivo_negativo():
    assert Calculadora().dividir(10, -2) == -5

def test_divisao_numero_negativo_positivo():
    assert Calculadora().dividir(-10, 2) == -5

def test_divisao_dois_numeros_negativos():
    assert Calculadora().dividir(-10, -2) == 5

def test_divisao_numero_com_zero():
    assert Calculadora().dividir(0, 5) == 0

def test_divisao_por_zero():
    assert Calculadora().dividir(5, 0) == "Erro: Divisão por zero não permitida!"

def test_divisao_zeros():
    assert Calculadora().dividir(0, 0) == "Erro: Divisão por zero não permitida!"

def test_divisao_numeros_decimais_positivos():
    assert Calculadora().dividir(10.5, 2.5) == 4.2

def test_divisao_numeros_decimais_negativos():
    assert Calculadora().dividir(-10.5, 2.5) == -4.2
