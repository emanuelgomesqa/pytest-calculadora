import math

class Calculadora:
    
    def adicionar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero não permitida!"
        return a / b
    
    def fatorial(self, a):
        if not isinstance(a, int):
            return "Erro: Fatorial só é definido para números inteiros!"
        if a < 0:
            return "Erro: Fatorial de número negativo não existe!"
        return math.factorial(a)

    
    def potencia(self, a, b):
        return a ** b