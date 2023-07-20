from funcoes import Soma
from funcoes import Subtracao
from funcoes import Divisao
from funcoes import Multiplicacao
from funcoes import Exponencial

def calcule(a,b,op):
    resultado = 0
    if type(a) == str or type(a) == bool:
        print("O numero precisa ser um inteiro ou um float.")
        resultado = "Não foi possivel obter um resultado."
        return resultado
    else:
        pass
    if type(b) == str or type(b) == bool:
        print("O numero precisa ser um inteiro ou um float.")
        resultado = "Não foi possivel obter um resultado."
        return resultado
    else:
        pass
    resultado = 0
    if op not in ['+','-','/','*','**']:
        print("Operação não identificada!")
        resultado = "Não foi possivel realizar a operação."
    elif op == '+':
        print(f"a soma é {Soma(a,b)}")
        resultado = Soma(a,b)
    elif op == '-':
        print(f"a subtração é {Subtracao(a,b)}")
        resultado = Subtracao(a,b)
    elif op == '/':
        print(f"a divisão é {Divisao(a,b)}")
        resultado = Divisao(a,b)
    elif op == '*':
        print(f"a multiplicação é {Multiplicacao(a,b)}")
        resultado = Multiplicacao(a,b)
    elif op == '**':
        print(f"a exponecial é {Exponencial(a,b)}")
        resultado = Exponencial(a,b)
    return resultado