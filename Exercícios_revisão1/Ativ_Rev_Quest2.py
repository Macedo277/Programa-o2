# Faça um Programa que verifique se uma letra digitada é vogal ou consoante

letra = input("Digite uma letra: ").lower()
vogal = ["a", "e", "i", "o", "u"]
consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

if letra in vogal: 
        print("A letra digitada é uma vogal")
elif letra in consoantes:
        print("A letra digitada é um consoante")
else:
        print("O digito informado não é uma letra")

# for i in consoantes:
#     if letra == i:
#         print("A letra digitada é uma consoante ")
#     else:   
#         print("O digito informado não é uma letra")