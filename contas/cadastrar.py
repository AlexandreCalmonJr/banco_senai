import sys
sys.path.append('..')
from dados import db

print("\n--- CADASTRO DE NOVA CONTA ---")
id_cliente_str = input("Digite o ID do cliente para vincular a conta: ")
tipo_conta = input("Digite o tipo da conta (Ex: Corrente, Poupança): ")

cliente_encontrado = None
try:
    id_cliente = int(id_cliente_str)
    for cliente in db['clientes']:
        if cliente['id_cliente'] == id_cliente:
            cliente_encontrado = cliente
            break
except ValueError:
    print("ID inválido.")

if cliente_encontrado:
    novo_id = db['proximo_id_conta']
    nova_conta = {
        'id_conta': novo_id,
        'id_cliente': id_cliente,
        'tipo_conta': tipo_conta,
        'saldo': 0.0,
        'movimentacoes': [], # Histórico de movimentações da conta
        'ativa': True
    }
    db['contas'].append(nova_conta)
    db['proximo_id_conta'] += 1
    print(f"\nConta tipo '{tipo_conta}' criada com sucesso para '{cliente_encontrado['nome_cliente']}'!")
else:
    print(f"\nCliente com ID {id_cliente_str} não encontrado.")