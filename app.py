

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
depositos = []
saques = []

while True: 

    opcao = input(menu)

    if opcao == "d":
        deposito = int(input("Informe o Valor do Deposito: "))
        if deposito > 0:
            saldo += deposito
            depositos.append(deposito)
            print(f"Depósito de R${deposito:.2f} realizado com sucesso!")
        else:
            print("O valor do deposito deve ser maior que zero. Tente Novamente!")
     
    
    elif opcao == "s":

        if numero_saques < LIMITE_SAQUES:
            saque = int(input("Informe o Valor do Saque: "))
            if saque > 0:
                if saque <= saldo:
                    if limite <= saque:
                        print("O limite de saque é de R$500,00.")
                    else:
                        saldo -= saque
                        saques.append(saque)
                        numero_saques += 1
                        print(f"Saque de R${saque:.2f} realizado com sucesso!")
                else:
                    print("Saldo insuficiente para realizar o saque.")
            else:
                print("O valor do saque deve ser maior que zero. Tente Novamente!")
        else:
            print("Você atingiu o limite máximo de saques.")


    elif opcao == "e":
        print(" ----- Extrato: ------ ")
        for valorDeposito in depositos:
            print(f"Deposito: R${valorDeposito:.2f}")
        
        for valorSaque in saques:
            print(f"Saque: R${valorSaque:.2f}")
        
        print(f"Saldo Atual: R${saldo: .2f}")
    

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")




