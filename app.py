

menu = """

-------  Menu: -----------
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True: 

    opcao = input(menu)

    if opcao == "d":
        deposito = int(input("Informe o Valor do Deposito: "))
        if deposito > 0:
            saldo += deposito
            print(f"Depósito de R${deposito:.2f} realizado com sucesso!")
        else:
            print("O valor do deposito deve ser maior que zero. Tente Novamente!")
     
    
    elif opcao == "s":
        print("Sacar")
    
    elif opcao == "e":
        print("Extrato")
    

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


print(saldo)

