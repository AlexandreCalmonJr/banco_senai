import sys
sys.path.append('..')
from dados import db

print("\n--- RELATÓRIO: MOVIMENTAÇÕES POR CONTA ---")

if not db['contas']:
    print("Nenhuma conta cadastrada para gerar relatório.")
else:
    print(f"{'ID Conta':<10} | {'Cliente':<25} | {'Nº de Movimentações':<20}")
    print("-" * 60)
    
    # Itera sobre cada conta para analisar suas transações
    for conta in db['contas']:
        nome_cliente = "[Cliente não encontrado]"
        # Encontra o nome do dono da conta
        for cliente in db['clientes']:
            if cliente['id_cliente'] == conta['id_cliente']:
                nome_cliente = cliente['nome_cliente']
                break
        
        contador_mov = 0
        # Conta quantas transações pertencem a esta conta
        for transacao in db['transacoes']:
            if transacao['id_conta'] == conta['id_conta']:
                contador_mov += 1
        
        print(f"{conta['id_conta']:<10} | {nome_cliente:<25} | {contador_mov:<20}")

print("-" * 60)