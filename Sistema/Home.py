# from funções import somar, subtrair
import funções
print("Digite a opção desejada: \n")
opcao = input("1 - somar \n 2 - subtrair")

a = int(input("Digite um número: "))
b = int(input("Digite um segundo número: "))

if opcao == "1":
    print(funções.somar(a,b))
elif opcao == "2":
    print(funções.subtrair(a,b))
