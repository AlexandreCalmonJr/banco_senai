# clientes/listar.py
import sys
sys.path.append('..')
from dados import db

print("\n--- LISTAGEM DE CLIENTES ---")

escolha = input("Deseja listar [T]odos os clientes ou [B]uscar um específico? ").upper()

if not db['clientes']:
    print("\nNenhum cliente cadastrado no momento.")

elif escolha == 'B':
    # Lógica ajustada para buscar um cliente específico
    print("\n--- BUSCA DE CLIENTE ---")
    termo_busca = input("Digite o nome ou CPF do cliente que deseja encontrar: ").lower()
    
    clientes_encontrados = []
    for cliente in db['clientes']:
        # AJUSTE: Buscando pelas novas chaves 'nome' e 'cpf'
        # AJUSTE: Convertendo o CPF (que é int) para string para a busca funcionar
        if termo_busca in cliente['nome'].lower() or termo_busca == str(cliente['cpf']) or termo_busca in str(cliente['id_cliente']):
            clientes_encontrados.append(cliente)

    if not clientes_encontrados:
        print(f"\nNenhum cliente encontrado com o termo '{termo_busca}'.")
    else:
        print("\n--- CLIENTES ENCONTRADOS ---")
        for cliente in clientes_encontrados:
            # AJUSTE: Convertendo o booleano 'pessoa_fisica' para um texto legível
            tipo_pessoa = "Física" if cliente['pessoa_fisica'] else "Jurídica"
            
            # AJUSTE: Imprimindo com as novas chaves
            print(f"ID: {cliente['id_cliente']} | Nome: {cliente['nome']} | CPF: {cliente['cpf']} | Tipo: {tipo_pessoa}")
        print("------------------------------")

elif escolha == 'T':
    # Lógica ajustada para listar todos os clientes
    print("\n--- LISTA COMPLETA DE CLIENTES ---")
    for cliente in db['clientes']:
        # AJUSTE: Convertendo o booleano 'pessoa_fisica' para um texto legível
        tipo_pessoa = "Física" if cliente['pessoa_fisica'] else "Jurídica"
        
        # AJUSTE: Imprimindo com as novas chaves
        print(f"ID: {cliente['id_cliente']} | Nome: {cliente['nome']} | CPF: {cliente['cpf']} | Tipo: {tipo_pessoa} | Idade: {cliente['idade']}")
    print("------------------------------------")
    
else:
    if db['clientes']:
        print("\nOpção inválida. Por favor, escolha 'T' ou 'B'.")