# Menu de opções
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Variáveis globais
saldo = 0
limite_saque = 500
historico_transacoes = ""
numero_saques_realizados = 0
LIMITE_SAQUES_DIARIO = 3

def depositar(valor):
    global saldo, historico_transacoes
    if valor > 0:
        saldo += valor
        historico_transacoes += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(valor):
    global saldo, numero_saques_realizados, historico_transacoes
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite_saque:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques_realizados >= LIMITE_SAQUES_DIARIO:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        historico_transacoes += f"Saque: R$ {valor:.2f}\n"
        numero_saques_realizados += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

def exibir_extrato():
    print("\n================ EXTRATO ================")
    if not historico_transacoes:
        print("Não foram realizadas movimentações.")
    else:
        print(historico_transacoes)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    while True:
        opcao = input(menu).lower()
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            depositar(valor)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            sacar(valor)
        elif opcao == "e":
            exibir_extrato()
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Executar o programa principal
if __name__ == "__main__":
    main()
