from desafiobancov3_1 import Conta
from desafiobancov3_2 import Transacao


class Cliente:
    def __init__(self, conta):
        self.usuario = {}
        self.lista_usuarios = []

        def realizar_transacao(self, conta, transacao):
            #transacao.registrar(conta)
            pass

        def adicionar_conta(self, conta):
            self.contas.append(conta)


        def filtrar_usuario(cpf, lista_usuarios):
            usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario["cpf"] == cpf]
            return usuarios_filtrados[0] if usuarios_filtrados else None


class ContaCorrente(Conta):
    def __init__(self):
        super().__init__()

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
            for k, v in conta.items():
                print(f'\033[1;31m{k} = {v}\033[m')


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf):
        super().__init__()
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def criar_usuario(lista_usuario):
        usuario = dict()
        usuario['cpf'] = int(input('Número do CPF:'))
        if filtrar_usuario(usuario['cpf'], lista_usuario) is None:
            usuario['nome'] = input('Nome do Usuário(a): ')
            usuario['data_nascimento'] = input("Informe a data de nascimento (dd-mm-aaaa): ")
            usuario['endereco'] = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            
        else:
            print('\033[1;31ERRO: Ao criar o usuário\033[m')


class menu:
    def __init__(self):
        pass
    def inicial(self):
        bancario = 'SISTEMA BANCÁRIO'
        menu = f"""\n\033[1;33m
        {'=' * 30}
        {bancario.center(30)}
        {'=' * 30}
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

    def exibir_extrato(saldo, /, *, extrato):
        print("\n\033[1;33m================ EXTRATO ================\033[m")
        print("\033[1;33mNão foram realizadas movimentações.\033[m" if not extrato else extrato)
        print(f"\n\033[1;33mSaldo: R$ {saldo:.2f}\033[m")
        print("\033[1;33m==========================================\033[m")

def main(menu):
    while True:
        menu().inicial()
        opcao = input().lower()
        match opcao:
            case "d":
                #valor = float(input("\n\033[1;33mInforme o valor do depósito: \033[m"))
                pass
            case "s":
                #valor = float(input("Informe o valor do saque: "))
                pass
            case "e":
                pass
            case "nc":
                pass
                '''usuario_cpf = ''
                if usuario_cpf:
                    pass
                else:
                    print('\033[1;31mERRO:Usuário com CPF inválido\033[m')'''
            case "lc":
                pass
            case "nu":
                pass
            case "q":
                break
            case _:
                print("\033[1;31mOperação inválida, por favor selecione novamente a operação desejada.\033[m")


main(menu)
