


print("""
============================================================================================
SIMULADOR BANCARIO
============================================================================================
""")

saldo_bancario = 0
extrato = ""
saques_diarios = 0

while True:

    print('''
[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair
 ''')

    menu = int(input("Selecione um número correspondente a opção: "))

    if (menu == 0):
        deposito = float(input("Digite o valor de depósito: "))

        if(deposito >= 0):
            saldo_bancario += deposito
            extrato += (f'+ R${deposito:.2f}\n')
            print(f'Você depositou R${deposito:.2f}! Seu saldo total é de R${saldo_bancario:.2f}!')
        else:
            print("O valor solicitado é inválido! Por favor, tente novamente!")

    elif (menu == 1):
        saque = float(input("Digite o valor aqui o valor que deseja sacar: "))
        saque_limite = 500
        
        if (saques_diarios >= 3):
            print("Você excedeu o limite diário de saque! Por favor, tente amanhã novamente!")
        
        elif (saque > saque_limite):
            print("O saque solicitado é maior do que seu limite de saque! Por favor, tente novamente!")
        
        elif (saque > saldo_bancario):
            print("O saque solicitado é maior do que o seu saldo bancário!")

        else:
            saques_diarios += 1
            saldo_bancario -= saque
            extrato += (f'- R${saque:.2f}\n')
            print(f'Você sacou R${saque:.2f}! Seu saldo total é de R${saldo_bancario:2f}!')

    elif (menu == 2):
        print(extrato)
        print(saldo_bancario)

    elif (menu == 3):
        break
    else:
        print("Opção inválida! Tente novamente!")

print("Saindo do sistema!")




