import sys
sys.path.append('..')
from dados import db

clientes = {}
print("\n--- CADASTRO DE CLIENTE ---")

nome_cliente = input("Digite seu nome completo: ")
idade_cliente = int(input("Digite sua idade: "))
cpf_cliente = int(input("Digite seu CPF: "))

# Pega o ID atual para este cliente
novo_id = (db['proximo_id_cliente'])

while True:
    tipo_cliente = input("É Pessoa Física ou Jurídica? (F para Física / J para Jurídica): ").upper()
    if tipo_cliente == 'F':
        clientes['pessoa_fisica'] = True
        break
    elif tipo_cliente == 'J':
        clientes['pessoa_fisica'] = False
        break
    else:
        print("Opção inválida. Por favor, digite 'F' ou 'J'.")

sexo_cliente = input("Sexo masculino(M) ou feminino(F): ").upper()

# Adiciona os dados ao dicionário do cliente
clientes['id_cliente'] = novo_id  # IMPORTANTE: adiciona o ID ao cliente
clientes['nome'] = nome_cliente
clientes['idade'] = idade_cliente
clientes['cpf'] = cpf_cliente
clientes['sexo'] = sexo_cliente

# Adiciona o cliente à lista
db['clientes'].append(clientes)

# IMPORTANTE: Incrementa o ID para o próximo cliente
db['proximo_id_cliente'] += 1

print(f"\nCLIENTE CADASTRADO! Cliente '{nome_cliente}' cadastrado com sucesso! ID: {novo_id}")

# Corrigido: fechou as aspas corretamente
abrir_conta = input(f"Deseja abrir uma conta para '{nome_cliente}' agora? (s/n): ").lower()

if abrir_conta == 's':
    tipo_conta = input("Qual o tipo da conta a ser aberta? (ex: Corrente, Poupança): ")
    
    # Pega o ID para a nova conta
    id_nova_conta = db['proximo_id_conta']
    
    # Cria o dicionário da nova conta, usando o 'novo_id' do cliente recém-criado
    nova_conta = {
        'id_conta': id_nova_conta,
        'id_cliente': novo_id,  # <== AQUI ESTÁ A LIGAÇÃO AUTOMÁTICA
        'tipo_conta': tipo_conta,
        'saldo': 0.0,
        'ativa': True
    }
    
    # Adiciona a nova conta à lista de contas
    db['contas'].append(nova_conta)
    
    # Incrementa o ID para a próxima conta
    db['proximo_id_conta'] += 1
    
    print(f"\nCONTA CRIADA! Uma conta '{tipo_conta}' foi aberta para o cliente. ID da Conta: {id_nova_conta}")
else:
    print("\nOK. O cliente foi criado sem uma conta associada neste momento.")
