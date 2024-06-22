bancario = 'SISTEMA BANCÁRIO'
menu = f"""\n\033[1;33m
{'='*30}
{bancario.center(30)}
{'='*30}
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
\033[m
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
mostrar_saques = ""
while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("\n\033[1;33mInforme o valor do depósito: \033[m"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("\033[1;31mOperação falhou! O valor informado é inválido.\033[m")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

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

        else:
            print("\033[1;31mOperação falhou! O valor informado é inválido.\033[m")

    elif opcao == "e":
        print("\n\033[1;33m================ EXTRATO ================\033[m")
        print("\033[1;33mNão foram realizadas movimentações.\033[m" if not extrato else extrato)
        print(f"\n\033[1;33mSaldo: R$ {saldo:.2f}\033[m")
        print("\033[1;33m==========================================\033[m")

    elif opcao == "q":
        break

    else:
        print("\033[1;31mOperação inválida, por favor selecione novamente a operação desejada.\033[m")
