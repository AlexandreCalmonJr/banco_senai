import sys
sys.path.append('..')
from dados import db

print("\n--- RELATÓRIO: CONTAS POR CLIENTE ---")

if not db['clientes']:
    print("Nenhum cliente cadastrado para gerar relatório.")
else:
    print(f"Total de clientes no banco: {len(db['clientes'])}")
    print("-" * 40)
    
    # Itera sobre cada cliente
    for cliente in db['clientes']:
        print(f"\nCliente: {cliente['nome_cliente']} (ID: {cliente['id_cliente']})")
        
        contas_do_cliente = []
        # Itera sobre todas as contas para encontrar as que pertencem a este cliente
        for conta in db['contas']:
            if conta['id_cliente'] == cliente['id_cliente']:
                contas_do_cliente.append(conta)
        
        if not contas_do_cliente:
            print("  -> Este cliente não possui contas.")
        else:
            print(f"  -> Total de contas: {len(contas_do_cliente)}")
            for conta in contas_do_cliente:
                print(f"    - ID Conta: {conta['id_conta']} | Tipo: {conta['tipo_conta']} | Saldo: R$ {conta['saldo']:.2f}")

print("-" * 40)