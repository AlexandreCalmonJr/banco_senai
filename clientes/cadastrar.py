# clientes/cadastrar.py
import sys
sys.path.append('..')
from dados import db

print("\n--- CADASTRO DE NOVO CLIENTE ---")
# Coleta de dados padronizada
nome = input("Nome do cliente: ")
idade_str = input("Idade: ")
cpf = input("CPF (apenas números): ")
tipo = input("Tipo (PF ou PJ): ").upper()
sexo = input("Sexo: ")

try:
    idade = int(idade_str)
    
    cpf_existe = False
    for cliente in db['clientes']:
        if cliente['cpf_cliente'] == cpf:
            cpf_existe = True
            break

    if cpf_existe:
        print(f"\nErro: CPF {cpf} já cadastrado.")
    elif tipo not in ['PF', 'PJ']:
        print("\nErro: Tipo de cliente inválido. Use PF ou PJ.")
    else:
        novo_id = db['proximo_id_cliente']
        # CORREÇÃO: Cria um dicionário novo para cada cliente
        novo_cliente = {
            'id_cliente': novo_id,
            'nome_cliente': nome,
            'idade_cliente': idade,
            'cpf_cliente': cpf,
            'tipo_cliente': tipo,
            'sexo_cliente': sexo
        }
        db['clientes'].append(novo_cliente)
        db['proximo_id_cliente'] += 1
        print(f"\nCLIENTE CADASTRADO! ID: {novo_id}")
        
        abrir_conta = input(f"Deseja abrir uma conta para '{nome}' agora? (s/n): ").lower()
        if abrir_conta == 's':
            tipo_conta = input("Qual o tipo da conta? (ex: Corrente, Poupança): ")
            id_nova_conta = db['proximo_id_conta']
            nova_conta = {
                'id_conta': id_nova_conta, 'id_cliente': novo_id,
                'tipo_conta': tipo_conta, 'saldo': 0.0, 'ativa': True
            }
            db['contas'].append(nova_conta)
            db['proximo_id_conta'] += 1
            print(f"\nCONTA CRIADA! ID da Conta: {id_nova_conta}")
except ValueError:
    print("\nErro: Idade deve ser um número.")