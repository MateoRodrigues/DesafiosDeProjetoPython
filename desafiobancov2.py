def menu():
    bancario = 'SISTEMA BANCÁRIO'
    menu = f"""\n\033[1;33m
    {'='*30}
    {bancario.center(30)}
    {'='*30}
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    \033[m
    => """
    print(menu, end='')

def depositar(saldo, valor, extrato ,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato

    else:
        print("\033[1;31mOperação falhou! O valor informado é inválido.\033[m")

def sacar(*, saldo,valor,extrato,limite,numero_saques,limite_saques):
    mostrar_saques = ""
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\033[1;31mOperação falhou! Você não tem saldo suficiente.\033[m")

    elif excedeu_limite:
        print(f"\033[1;31mOperação falhou! O valor do saque é de {valor:.2f} excede o limite que é de 500.\033[m")

    elif excedeu_saques:
        print("\033[1;31mOperação falhou! Número máximo de saques excedido.\033[m")
        print(mostrar_saques)

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        mostrar_saques += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        saque_realizado = {}
        saque_realizado['numero_saques'] = numero_saques
        saque_realizado['saldo'] = saldo
        saque_realizado['extrato'] = extrato
        return saque_realizado

    else:
        print("\033[1;31mOperação falhou! O valor informado é inválido.\033[m")

def exibir_extrato(saldo,/,*, extrato):
    print("\n\033[1;33m================ EXTRATO ================\033[m")
    print("\033[1;33mNão foram realizadas movimentações.\033[m" if not extrato else extrato)
    print(f"\n\033[1;33mSaldo: R$ {saldo:.2f}\033[m")
    print("\033[1;33m==========================================\033[m")

def criar_usuario(lista_usuario):
    usuario = dict()
    usuario['cpf'] = int(input('Número do CPF:'))
    if filtrar_usuario(usuario['cpf'],lista_usuario) is None:
        usuario['nome'] = input('Nome do Usuário(a): ')
        usuario['data_nascimento'] = input("Informe a data de nascimento (dd-mm-aaaa): ")
        usuario['endereco'] = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        return usuario
    else:
        print('\033[1;31ERRO: Ao criar o usuário\033[m')

def filtrar_usuario(cpf, lista_usuarios):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(AGENCIA, numero_conta, usuario_cpf, lista_contas):
    conta = {}
    if (len(AGENCIA) == 4) and ((numero_conta not in lista_contas) or (usuario_cpf == None)):
        conta['agencia'] = AGENCIA
        conta['numero_da_conta'] = numero_conta
        conta['usuario'] = usuario_cpf
        return conta
    else:
        print('\033[1;31mERRO: Não foi possível criar usuário\033[m ')


def listar_contas(contas):
    for conta in contas:
        for k,v in conta.items():
            print(f'\033[1;31m{k} = {v}\033[m')
def main():
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuario = {}
    lista_usuarios = []
    contas = []
    while True:
        menu()
        opcao = input().lower()
        match opcao:
            case "d":
                valor = float(input("\n\033[1;33mInforme o valor do depósito: \033[m"))
                saldo, extrato = depositar(saldo, valor, extrato)
            case "s":
                valor = float(input("Informe o valor do saque: "))
                saque = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
                saldo = saque['saldo']
                extrato = saque['extrato']
                numero_saques = saque['numero_saques']
            case "e":
                exibir_extrato(saldo, extrato=extrato)
            case "nc":
                numero_conta = len(contas) + 1
                usuario_cpf = filtrar_usuario(int(input("\033[1;33mDigite o número de CPF do usuário(a):\033[m")),lista_usuarios)
                if usuario_cpf:
                    contas.append(criar_conta(AGENCIA, numero_conta, usuario_cpf, contas))
                else:
                    print('\033[1;31mERRO:Usuário com CPF inválido\033[m')
            case "lc":
                listar_contas(contas)
            case "nu":
                lista_usuarios.append(criar_usuario(lista_usuarios))
            case "q":
                break
            case _:
                print("\033[1;31mOperação inválida, por favor selecione novamente a operação desejada.\033[m")


main()
