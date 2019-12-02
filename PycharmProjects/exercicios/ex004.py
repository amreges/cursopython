# funcao "input" sempre retorna um tipo "str"

a = input("Digite algo: ")
print("O tipo primitivo desse valor é: ", type(a))
print("Só tem espacos: ", a.isspace())
print(" É um numero? ", a.isnumeric())
print("É alfabetico? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("Está em maiúsculas? ", a.isupper())
print("Está em minúsculas? ", a.islower())
