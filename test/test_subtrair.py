import pytest
from calculadora import Calculadora

def test_subtracao_numeros_positivos_menor_maior():
    assert Calculadora().subtrair(2, 5) == -3

def test_subtracao_numeros_positivos_maior_menor():
    assert Calculadora().subtrair(5, 2) == 3

def test_subtracao_numero_positivo_negativo():
    assert Calculadora().subtrair(5, -3) == 8

def test_subtracao_numero_negativo_positivo():
    assert Calculadora().subtrair(-5, 2) == -7

def test_subtracao_dois_numeros_negativos():
    assert Calculadora().subtrair(-4, -6) == 2

def test_subtracao_numero_com_zero():
    assert Calculadora().subtrair(0, 5) == -5

def test_subtracao_zeros():
    assert Calculadora().subtrair(0, 0) == 0

def test_subtracao_numeros_decimais_positivos():
    assert Calculadora().subtrair(12.000001, 3.500002) == 8.49999899999999 #Esse é um exemplo errado que dará errado, apenas para validar a execução possuindo um erro.

def test_subtracao_numeros_decimais_negativos():
    assert Calculadora().subtrair(-3.000001, 5.500001) == -8.500002