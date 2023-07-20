from funcoes import Soma
from funcoes import Subtracao
from funcoes import Divisao
from funcoes import Multiplicacao
from funcoes import Exponencial

def calcule(a,b,operacao):
    resultado = 0
    if type(a) == str or type(a) == bool:
        print("Digite um numero por favor.")
        resultado = "Não foi possivel fazer operação"
        return resultado
    else:
        pass
    if type(b) == str or type(b) == bool:
        print("Digite um numero por favor.")
        resultado = "Não foi possivel fazer operação"
        return resultado
    else:
        pass
    if operacao not in ['+','-','/','*','**']:
        print("Operação não identificada!")
        resultado = "Não foi possivel realizar a operação."
    elif operacao == '+':
        print(f"a soma é {Soma(a,b)}")
        resultado = Soma(a,b)
    elif operacao == '-':
        print(f"a subtração é {Subtracao(a,b)}")
        resultado = Subtracao(a,b)
    elif operacao == '/':
        print(f"a divisão é {Divisao(a,b)}")
        resultado = Divisao(a,b)
    elif operacao == '*':
        print(f"a multiplicação é {Multiplicacao(a,b)}")
        resultado = Multiplicacao(a,b)
    elif operacao == '**':
        print(f"a exponecial é {Exponencial(a,b)}")
        resultado = Exponencial(a,b)
    return resultado

calcule()
