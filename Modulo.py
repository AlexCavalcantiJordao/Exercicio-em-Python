# Modulo Principal
import modifunções
import random

modifunções.mensagem()

n = random.randint(1, 10)

numero = int(input("Digite um número inteiro: "))
print("Calculando o fatorial do número: ")
fat = modifunções.fatorial(n)
print("O fatorial é ", n, "é ",fat)

print("Calculando a sequência de Fibonacci: ")
fib = modifunções.fibo(n)
print("O Fibonacci é ", fib)
