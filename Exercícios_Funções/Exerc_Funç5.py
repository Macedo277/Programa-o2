# 5. Escreva um programa que possa cadastrar clientes ou funcionários para uma
# loja. Se o usuário quiser cadastrar um cliente, dados de nome, endereço,
# CPF devem ser solicitados. Caso o usuário prefira adicionar um novo
# funcionário, dados de nome, salário, cargo e CPF devem ser requisitados.
# Utilize comandos de manipulação de string para personalizar a saída.

def cliente():
    dados = []
    dados.append(input("Digite o nome do cliente: "))
    dados.append(input("Digite o CPF do cliente: "))
    dados.append(input("Digite o Endereço do cliente: "))
    print(f"Os dados do cliente são: \nNome: {dados[0]}, CPF: {dados[1]}, endereço: {dados[2]}")

def funci():
    dados = []
    dados.append(input("Digite o nome do funcionário: "))
    dados.append(input("Digite o CPF do funcionário: "))
    dados.append(input("Digite o endereço do funcionário: "))
    print