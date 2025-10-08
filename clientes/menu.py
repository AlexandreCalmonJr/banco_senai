# Menu para CRUD de clientes

import os

print("\n--- MENU CLIENTES ---")

while True:
    
    print("""
    --- GESTÃO DE CLIENTES ---
    [1] Cadastrar Novo Cliente1
    [2] Listar Clientes
    [3] Editar Cliente
    [4] Deletar Cliente
    [0] Voltar ao Menu Principal
    """)
    
    opcao_cliente = input("Escolha uma ação => ")

    if opcao_cliente == '1':
        exec(open('clientes/cadastrar.py', encoding='utf-8').read())
    elif opcao_cliente == '2':
        exec(open('clientes/listar.py', encoding='utf-8').read())
    elif opcao_cliente == '3':
        exec(open('clientes/editar.py', encoding='utf-8').read())
    elif opcao_cliente == '4':
        exec(open('clientes/deletar.py', encoding='utf-8').read())
    elif opcao_cliente == '0':
        print("\nRetornando ao menu principal...")
        break 
    else:
        print("\nOpção inválida!")
        
    input("\nPressione Enter para continuar...")