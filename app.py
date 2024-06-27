
def sacar(*, saldo, valor, extrato, limite, numero_saques, saques, LIMITE_SAQUES):
    if numero_saques >= LIMITE_SAQUES:
        print("Você atingiu o limite máximo de saques.")
        return saldo, extrato, numero_saques
    
    if valor > saldo:
        print("Saldo insuficiente!")
        return saldo, extrato, numero_saques

    if valor > limite:
        print("O limite de saque é de R$500,00.")
        return saldo, extrato, numero_saques
    
    if valor > 0:
        saldo -= valor
        extrato.append(f"Saque: -R${valor: .2f}")
        saques.append(valor)
        numero_saques += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
        print("O valor do saque deve ser maior que zero. Tente Novamente!")
    
    return saldo, extrato, numero_saques

def depositar(saldo, /, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito de R${valor:.2f} realizado com sucesso!")
        return saldo, extrato
    else:
        print("O valor do deposito deve ser maior que zero. Tente Novamente!")
        return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print(" ----- Extrato: ------ ")
    for transacao in extrato:
        print(transacao)
        print(f"Saldo Atual: R${saldo:.2f}")


usuarios = []
contas = []
numero_conta = 1
AGENCIA = "0001"

def criar_usuario(nome, data_nascimento, cpf, endereco):
    cpf = ''.join(filter(str.isdigit, cpf))
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado.")
            return

    usuario = {
        "nome" : nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")


def criar_conta(cpf):
    global numero_conta

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            conta = {
                "agencia": AGENCIA,
                "numero_conta": numero_conta,
                "usuario": usuario,
                "saldo": 0,
                "extrato": [],
                "limite": 500,
                "numero_saques": 3
            }
            contas.append(conta)
            numero_conta += 1
            print("Conta corrente criada com sucesso!")
            return
    
    print("Usuário não encontrado. Verifique o CPF e tente novamente.")


def listar_contas():
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}")
        

menu = """

-------  Menu: -----------
[u] Cadastrar Usuário
[c] Criar Conta Corrente
[d] Depositar
[s] Sacar
[e] Extrato
[l] Listar Contas
[q] Sair

"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
depositos = []
saques = []

while True: 

    opcao = input(menu)

    if opcao == "u":
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento: ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")
        criar_usuario(nome, data_nascimento, cpf, endereco)
    
    elif opcao == "c":
        cpf = input("Informe o CPF do usuário: ")
        criar_conta(cpf)

    elif opcao == "d":
        valor = float(input("Informe o Valor do Deposito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    
    
    elif opcao == "s":
        valor = int(input("Informe o Valor do Saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo, valor=valor, extrato=extrato,
            limite=limite, numero_saques=numero_saques,
            saques=saques, LIMITE_SAQUES=LIMITE_SAQUES
        )


    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)
    
    elif opcao == "l":
        listar_contas()
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")




