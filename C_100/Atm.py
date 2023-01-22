sim = "sim"
não = "não"

print("Bem-vindo(a) a caixa ATM!")
input("Numero do cartão: ")
input("Senha do cartão: ")
print("Bem-vindo(a) a sua conta! ")
saldo = input("Quer ver seu saldo? ")
if saldo == "sim":
    print("Seu saldo é de 50000")
    retirada = input("Deseja retirar? ")
    if retirada == "sim":
        quantidade = int(input("Quanto? "))
        print("Seu saldo restante é de",50000-quantidade)