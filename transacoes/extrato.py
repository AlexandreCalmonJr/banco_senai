import sys
sys.path.append('..')
from dados import db

print("\n--- EXTRATO DA CONTA ---")
id_conta_str = input("Digite o ID da conta para ver o extrato: ")

conta_encontrada = None
try:
    id_conta = int(id_conta_str)
    for conta in db['contas']:
        if conta['id_conta'] == id_conta:
            conta_encontrada = conta
            break
except ValueError:
    print("ID inválido.")

if conta_encontrada:
    print("-" * 40)
    print(f"Extrato da Conta ID: {conta_encontrada['id_conta']} | Saldo Atual: R$ {conta_encontrada['saldo']:.2f}")
    print("-" * 40)
    transacoes_encontradas = False
    for transacao in db['transacoes']:
        if transacao['id_conta'] == id_conta:
            print(f"Data: {transacao['data']} | Tipo: {transacao['tipo_trans']:<10} | Valor: R$ {transacao['valor_trans']:8.2f}")
            transacoes_encontradas = True
    if not transacoes_encontradas:
        print("Nenhuma transação encontrada para esta conta.")
    print("-" * 40)
else:
    print(f"Conta com ID {id_conta_str} não encontrada.")
