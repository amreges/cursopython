# Desenvolva um programa que leia as suas notas de um aluno, calcule e mostre a sua média.
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
print("A média entre {:.1f} e {:.1f} é igual a {:.1f}".format(n1, n2, media))
# {:.1f} significa depois do ponto flutuante coloque apenas um digito