# Faça um programa que receba três números do usuário, e identifique o maior
# através de uma função e o menor número através de outra função.

def Maior(lista):
   return max(lista) 

num1 = int(input("Digite o primeiro número do usuário: "))
num2 = int(input("Digite o segundo número do usuário: "))
num3 = int(input("Digite o terceiro número do usuário: "))


lista = [num1, num2, num3]
max(lista) 
print(Maior(lista))
