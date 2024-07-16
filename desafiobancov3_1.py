from abc import ABC, abstractclassmethod, abstractproperty
class Conta:
    def __init__(self):
        self.AGENCIA = "0001"
        self._saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        self.contas = []

    def depositar(self, valor, /):
        if valor > 0:
            self._saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            return self._saldo, self.extrato

        else:
            print("\033[1;31mOperação falhou! O valor informado é inválido.\033[m")

    def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
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

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
