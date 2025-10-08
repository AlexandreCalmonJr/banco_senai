import sys
sys.path.append('..')
from dados import db

print("\n--- RANKING DE CLIENTES POR Nº DE TRANSAÇÕES ---")

if not db['clientes']:
    print("Nenhum cliente cadastrado para gerar o ranking.")
else:
    ranking = []
    # Para cada cliente, conta o número de transações em todas as suas contas
    for cliente in db['clientes']:
        num_transacoes = 0
        # Encontra as contas deste cliente
        for conta in db['contas']:
            if conta['id_cliente'] == cliente['id_cliente']:
                # Conta as transações para esta conta
                for transacao in db['transacoes']:
                    if transacao['id_conta'] == conta['id_conta']:
                        num_transacoes += 1
        ranking.append({'nome': cliente['nome_cliente'], 'transacoes': num_transacoes})

    # Ordena a lista de ranking do maior para o menor (usando Bubble Sort)
    n = len(ranking)
    for i in range(n):
        for j in range(0, n-i-1):
            if ranking[j]['transacoes'] < ranking[j+1]['transacoes']:
                ranking[j], ranking[j+1] = ranking[j+1], ranking[j]
    
    print(f"\n{'Posição':<10} | {'Cliente':<30} | {'Nº de Transações':<20}")
    print("-" * 70)
    
    pos = 1
    for item in ranking:
        print(f"{str(pos) + 'º':<10} | {item['nome']:<30} | {item['transacoes']:<20}")
        pos += 1
    
    print("-" * 70)
