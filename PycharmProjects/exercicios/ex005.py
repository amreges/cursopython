# Faca um porgrama que leia um numero inteiro e na tela o seu sucessor e o seu antecessor
n = int(input("digite um numero: "))
a = n - 1
s = n + 1
# Os dois prints estao corretos
print("Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}".format(n, a, s))
#segunda maneira
print("Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}".format(n, (n-1), (n+1)))
# Segundo print nao preciso utilisar as variaveis
