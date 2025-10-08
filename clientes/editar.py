import sys
sys.path.append('..')
from dados import db

print("\n--- EDITAR CLIENTE ---")
id_cliente_str = input("Digite o ID do cliente que deseja editar: ")

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
    print(f"\nEditando cliente: {cliente_encontrado['nome_cliente']}")
    print("Deixe em branco para manter o valor atual.")
    novo_nome = input(f"Novo nome ({cliente_encontrado['nome_cliente']}): ")
    if novo_nome: cliente_encontrado['nome_cliente'] = novo_nome
    # Adicione outros campos para editar aqui...
    print("\nCliente atualizado com sucesso!")
else:
    print(f"\nCliente com ID {id_cliente_str} não encontrado.")