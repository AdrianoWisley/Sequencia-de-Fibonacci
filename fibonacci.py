def pertence_fibonacci(num):
    a, b = 0, 1
    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
    return False

# Obtendo o número a ser verificado
numero = int(input("digite um número: "))

# Verificando se o número pertence à sequência
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequêcia de Fibonacci.")
    