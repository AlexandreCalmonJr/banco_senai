# clientes/listar.py
import sys
sys.path.append('..')
from dados import db

print("\n--- LISTAGEM DE CLIENTES ---")
escolha = input("Deseja listar [T]odos os clientes ou [B]uscar um específico? ").upper()

if not db['clientes']:
    print("\nNenhum cliente cadastrado.")
elif escolha == 'B':
    termo_busca = input("Digite o nome ou CPF do cliente: ").lower()
    clientes_encontrados = []
    for cliente in db['clientes']:
        if termo_busca in cliente['nome_cliente'].lower() or termo_busca == cliente['cpf_cliente']:
            clientes_encontrados.append(cliente)
    if not clientes_encontrados:
        print(f"\nNenhum cliente encontrado com o termo '{termo_busca}'.")
    else:
        print("\n--- CLIENTES ENCONTRADOS ---")
        for cliente in clientes_encontrados:
            print(f"ID: {cliente['id_cliente']} | Nome: {cliente['nome_cliente']} | CPF: {cliente['cpf_cliente']}")
elif escolha == 'T':
    print("\n--- LISTA COMPLETA DE CLIENTES ---")
    for cliente in db['clientes']:
        print(f"ID: {cliente['id_cliente']} | Nome: {cliente['nome_cliente']} | CPF: {cliente['cpf_cliente']} | Tipo: {cliente['tipo_cliente']}")
else:
    if db['clientes']: print("\nOpção inválida.")