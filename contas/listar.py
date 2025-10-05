import sys
sys.path.append('..')
from dados import db

print("\n--- LISTA DE CONTAS CADASTRADAS ---")
if not db['contas']:
    print("Nenhuma conta cadastrada no momento.")
else:
    for conta in db['contas']:
        nome_cliente = "Cliente não encontrado"
        for cliente in db['clientes']:
            if cliente['id_cliente'] == conta['id_cliente']:
                nome_cliente = cliente['nome_cliente']
                break
        
        status = "Ativa" if conta['ativa'] else "Inativa"
        print(f"ID Conta: {conta['id_conta']} | Tipo: {conta['tipo_conta']} | Cliente: {nome_cliente} | Saldo: R$ {conta['saldo']:.2f} | Status: {status}")
print("---------------------------------------")