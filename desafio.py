from datetime import datetime


menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair


=>"""
data_atual = datetime.today().strftime('%d-%m-%Y')
valor = 0
saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    if data_atual != datetime.today().strftime('%d-%m-%Y'):
        data_atual = datetime.today().strftime('%d-%m-%Y')
        numero_saques = 0

    opcao = input(menu)

    #Depósito
    if opcao == '1':
        print("Depósito")
        valor = float(input("Digite o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"{datetime.today().strftime('%d-%m-%Y %H:%M:%S')} Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor do deposito é inválido.")

    #Saque
    elif opcao == '2':
        print("Saque")
        
        #Se não estiver no limite de saque diário, a operação é cancelada no início
        if numero_saques < LIMITE_SAQUES:
            
            valor = float(input("Digite o valor para saque: "))

            #Teste: se o não ultapassou o limite do valor
            if valor > LIMITE:
                print("Operação falhou! O valor informado é maior que o limite para saque.")
            
            #Teste: se o saldo é suficiente 
            elif valor > saldo:
                print("Operação falhou! Saldo insuficiente.")

            #Passou pelos testes e será processado o saque
            elif valor > 0:
                numero_saques += 1
                saldo -= valor
                extrato += f"{datetime.today().strftime('%d-%m-%Y %H:%M:%S')} Saque: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! Valor digitado é inválido.")

        else:
            print("Operação falhou! O número de saque diário exedido.")

    #Extrato
    elif opcao == '3':
        print("\n-------------------Extrato-------------------")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print("---------------------------------------------")
        print(f"Saldo: R$ {saldo:.2f}")
        print("---------------------------------------------")

    #Sair    
    elif opcao == '4':
        print("Sair")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")