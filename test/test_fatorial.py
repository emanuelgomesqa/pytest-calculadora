import pytest
from calculadora import Calculadora

def test_fatorial_numero_positivo():
    assert Calculadora().fatorial(5) == 120

def test_fatorial_numero_zero():
    assert Calculadora().fatorial(0) == 1

def test_fatorial_numero_negativo():
    assert Calculadora().fatorial(-5) == "Erro: Fatorial de número negativo não existe!"

def test_fatorial_numero_decimal():
    assert Calculadora().fatorial(5.5) == "Erro: Fatorial só é definido para números inteiros!"

def test_fatorial_numeros_grandes():
    assert Calculadora().fatorial(20) == 2432902008176640000
