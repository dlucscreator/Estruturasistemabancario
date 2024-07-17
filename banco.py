import textwrap


class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        return self.contas


class Conta:
    def __init__(self, agencia, numero, cliente):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.extrato = ""
        self.limite = 500
        self.numero_saques = 0
        self.limite_saques = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.limite_saques

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")


class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        if self.filtrar_cliente(cliente.cpf):
            print("\n@@@ Já existe cliente com esse CPF! @@@")
        else:
            self.clientes.append(cliente)
            print("=== Cliente criado com sucesso! ===")

    def filtrar_cliente(self, cpf):
        clientes_filtrados = [cliente for cliente in self.clientes if cliente.cpf == cpf]
        return clientes_filtrados[0] if clientes_filtrados else None

    def adicionar_conta(self, conta):
        if self.filtrar_cliente(conta.cliente.cpf):
            self.contas.append(conta)
            conta.cliente.adicionar_conta(conta)
            print("\n=== Conta criada com sucesso! ===")
        else:
            print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")

    def listar_contas(self):
        for conta in self.contas:
            linha = f"""\
                Agência:\t{conta.agencia}
                C/C:\t\t{conta.numero}
                Titular:\t{conta.cliente.nome}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo cliente
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def main():
    banco = Banco()

    while True:
        opcao = menu()

        if opcao == "d":
            cpf = input("Informe o CPF do cliente: ")
            cliente = banco.filtrar_cliente(cpf)
            if cliente:
                numero_conta = int(input("Informe o número da conta: "))
                conta = next(conta for conta in cliente.listar_contas() if conta.numero == numero_conta)
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)
            else:
                print("\n@@@ Cliente não encontrado! @@@")

        elif opcao == "s":
            cpf = input("Informe o CPF do cliente: ")
            cliente = banco.filtrar_cliente(cpf)
            if cliente:
                numero_conta = int(input("Informe o número da conta: "))
                conta = next(conta for conta in cliente.listar_contas() if conta.numero == numero_conta)
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor)
            else:
                print("\n@@@ Cliente não encontrado! @@@")

        elif opcao == "e":
            cpf = input("Informe o CPF do cliente: ")
            cliente = banco.filtrar_cliente(cpf)
            if cliente:
                numero_conta = int(input("Informe o número da conta: "))
                conta = next(conta for conta in cliente.listar_contas() if conta.numero == numero_conta)
                conta.exibir_extrato()
            else:
                print("\n@@@ Cliente não encontrado! @@@")

        elif opcao == "nu":
            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            cpf = input("Informe o CPF (somente números): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            cliente = Cliente(nome, data_nascimento, cpf, endereco)
            banco.adicionar_cliente(cliente)

        elif opcao == "nc":
            cpf = input("Informe o CPF do cliente: ")
            cliente = banco.filtrar_cliente(cpf)
            if cliente:
                numero_conta = len(banco.contas) + 1
                conta = Conta("0001", numero_conta, cliente)
                banco.adicionar_conta(conta)
            else:
                print("\n@@@ Cliente não encontrado! @@@")

        elif opcao == "lc":
            banco.listar_contas()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
