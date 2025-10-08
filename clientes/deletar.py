import sys
sys.path.append('..')
from dados import db

print("\n--- DELETAR CLIENTE ---")

id_cliente = int(input("Digite o ID do cliente: "))
cliente_desejado = None   
for cliente in db['clientes']:
    if cliente['id_cliente'] == id_cliente: # Aqui vai puxar o id do cliente do banco de dados
        cliente_desejado = cliente
        break
if cliente_desejado:
    db['clientes'].remove(cliente_desejado)
    print(f"Cliente com ID {id_cliente} deletado com sucesso.")
else:
    print(f"O ID {id_cliente} não existe.")    

input("Pressione Enter para continuar...")



