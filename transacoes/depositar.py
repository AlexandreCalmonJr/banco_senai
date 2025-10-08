import sys, datetime
sys.path.append('..')
from dados import db

print("\n--- DEPÓSITO ---")
id_conta_str = input("Digite o ID da conta de destino: ")
valor_str = input("Digite o valor a ser depositado: ")

conta_encontrada = None
try:
    id_conta = int(id_conta_str)
    valor = float(valor_str)
    if valor <= 0:
        print("\nErro: O valor deve ser positivo.")
    else:
        for conta in db['contas']:
            if conta['id_conta'] == id_conta and conta['ativa']:
                conta_encontrada = conta
                break
        if conta_encontrada:
            conta_encontrada['saldo'] += valor
            transacao = {'id_transacao': db['proximo_id_transacao'], 'id_conta': id_conta, 'tipo_trans': 'Depósito', 'valor_trans': valor, 'data': str(datetime.datetime.now())}
            db['transacoes'].append(transacao)
            db['proximo_id_transacao'] += 1
            print(f"\nDepósito de R$ {valor:.2f} realizado! Novo saldo: R$ {conta_encontrada['saldo']:.2f}")
        else:
            print(f"\nConta com ID {id_conta_str} não encontrada ou inativa.")
except ValueError:
    print("\nErro: ID da conta ou valor inválido.")