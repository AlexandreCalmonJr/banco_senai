import os

while True:
    
    print("""
    --- GESTÃO DE CONTAS ---
    [1] Cadastrar Nova Conta
    [2] Listar Contas
    [3] Ativar/Desativar Conta
    [4] Deletar Conta
    [0] Voltar ao Menu Principal
    """)
    
    opcao_conta = input("Escolha uma ação => ")

    if opcao_conta == '1':
        exec(open('contas/cadastrar.py', encoding='utf-8').read())
    elif opcao_conta == '2':
        exec(open('contas/listar.py', encoding='utf-8').read())
    elif opcao_conta == '3':
        exec(open('contas/editar.py', encoding='utf-8').read())
    elif opcao_conta == '4':
        exec(open('contas/deletar.py', encoding='utf-8').read())
    elif opcao_conta == '0':
        print("\nRetornando ao menu principal...")
        break 
    else:
        print("\nOpção inválida!")
        
    input("\nPressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')