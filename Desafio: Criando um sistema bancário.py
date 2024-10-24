# Desafio: Criando um sistema bancário

# Objetivo Geral: Cria um sistema bancário com as operações: sacar, depositar e visualizar extrato.

# Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

# Operação deDeposito: 
# Deve ser possível depositar valores positivos para minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, desta forma não precisamo nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

# Operação de Saque: 
# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 reais por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato.

# Operação de extrato:
# Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem devem ser exibidos o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

print('='*50)
print('Banco NTT-DATA'.center(50))
print('='*50)

menu = """
            Menu 
Escolha uma das opções abaixo:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = saque = deposito= 0
limite = 500
extrato = ""
numero_saques = num_dep =  0
LIMITE_SAQUES = 3
sair = False
while True:

    opcao = input(menu)

    if opcao == "d":
        num_dep += 1
        while True:
            deposito = float(input('Digite o valor que deseja depositar: '))
            if deposito < 0:
                print('Valor invalido! Tente novamente.')
            else:
                break
        saldo += deposito
        print(f'Valor depositado R$ {deposito:.2f} reais')
        print('-.'*25)
        nova_op = str(input('Deseja realizar uma nova operação? [S/N] ')).lower()[0]
        if nova_op in 'n':
            break
        print('-.'*25)
        
    elif opcao == "s":
        numero_saques += 1
        while True:
            valor_sacado = float(input('Digite o valor que deseja sacar: '))
            if valor_sacado < 0:
                    print('Valor invalido! Tente novamente.')
            elif valor_sacado > limite:
                print(f'O limite de saque é de R$ {limite:.2f} reais.')
            else:
                break
        if numero_saques > LIMITE_SAQUES:
            print('Você atingiu o limite diário de saques.')
            break
        saque += valor_sacado 
        print(f'O valor sacado foi de R$ {valor_sacado:.2f} reais, você já realizou {numero_saques} saques.')
        nova_op = str(input('Deseja realizar uma nova operação? [S/N] ')).lower()[0]
        if nova_op in 'n':
            break
        print('-.'*25)
        saldo = saldo - saque
    
    elif opcao == "e":
        print('='*21, end='')
        print(' Extrato '.center(7), end='')
        print('='*21)
        print(f"Depósito:       R$ {deposito:>7.2f}")
        print(f'Saque           R$ {saque:>7.2f}')
        print("\n")  # Linha em branco
        print(f"Saldo:          R$ {saldo:>7.2f}")
        print("=" * 50)
        nova_op = str(input('Deseja realizar uma nova operação? [S/N] ')).lower()[0]
        if nova_op in 'n':
            break
        print('-.'*25)
    
    elif opcao == "q":
        break

    else:
        print('Operação inválida, por favor selecione novamente a opção desejada.')
print('Obrigado por utilizar nossos estabelecimentos.')