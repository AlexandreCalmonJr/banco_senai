
import sys
import datetime
sys.path.append('..')
from dados import db

print("\n--- APLICANDO RENDIMENTO DA POUPANÇA ---")

taxa = db['config']['taxa_rendimento_poupanca']
contas_afetadas = 0

for conta in db['contas']:
    # Aplica somente a contas do tipo 'Poupança' com saldo positivo
    if conta['tipo_conta'].lower() == 'poupança' and conta['saldo'] > 0:
        rendimento = conta['saldo'] * taxa
        saldo_anterior = conta['saldo']
        conta['saldo'] += rendimento
        contas_afetadas += 1
        
        # Cria um registro da transação de rendimento
        nova_transacao = {
            'id_transacao': db['proximo_id_transacao'],
            'id_conta': conta['id_conta'],
            'tipo_trans': 'Rendimento',
            'valor_trans': rendimento,
            'data': str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        }
        db['transacoes'].append(nova_transacao)
        db['proximo_id_transacao'] += 1

        print(f"Conta ID {conta['id_conta']}: Saldo anterior R${saldo_anterior:.2f}, Rendimento +R${rendimento:.2f}, Novo Saldo R${conta['saldo']:.2f}")

if contas_afetadas > 0:
    print(f"\nRendimento de {taxa*100}% aplicado com sucesso a {contas_afetadas} conta(s) poupança.")
else:
    print("\nNenhuma conta poupança com saldo positivo foi encontrada para aplicar o rendimento.")