#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
n = int(input("Digite um numero: "))
d = n * 2
t = n * 3
r = n ** (1/2)
print("O dobro de {} vale {}".format(n, d))
print("O triplo de {} vale {}".format(n, t))
print(" A raiz quadrada de {} é igual a {}".format(n, r))
# segunda maneira

print("O dobro de {} vale {}".format(n, (n*2)))
print("O dobro de {} vale {}. \nA raiz quadrada de {} é a {:.2f}.".format(n, (n*3), n, pow(n,(1/2))))
# {:.2f} quantidade de casa decimais
# pow outra funcao para raiz quadrada
# \n quebra de linha
