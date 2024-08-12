# Faça um programa que calcule a área de um terreno e imprima na tela. 

def area(comprimento, largura):
    area = comprimento * largura
    return area

comprimento = float(input("Digite o comprimento: "))
largura = float(input("Digite a largura: "))

print(area(comprimento, largura))