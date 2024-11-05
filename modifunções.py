# Módulo com funções variadas...

# Funções que exibe mensagem de boas-vindas:
def mensagem():
    print("Bóson Treinamentos em Tecnologias! \n")

# Funções para cálculos dp fatorial de um número:
def fatorial(numero):
    if(numero < 0):
        return "Digite um valor maior ou igual a zero - (0)"
    else:
        return numero * fatorial(numero - 1)

# Função para retornar uma série de Fibonacci até um valor x:
def fibo(n):
    resultado = [0]
    a, b = 0, 1
    while (b < n):
        resultado.append(b)
        a, b = b, a + b
    return resultado
