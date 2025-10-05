import os

while True:
    print("""
    --- GESTÃO DE CONTAS ---
    [1] Cadastrar Nova Conta
    [2] Listar Todas as Contas
    [3] Ativar/Desativar uma Conta
    [4] Deletar uma Conta
    [0] Voltar ao Menu Principal
    """)
    
    opcao_conta = input("Escolha uma ação => ")
    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao_conta == '1':
        exec(open('contas/cadastrar.py', encoding='utf-8').read())
    elif opcao_conta == '2':
        exec(open('contas/listar.py', encoding='utf-8').read())
    elif opcao_conta == '3':
        exec(open('contas/editar.py', encoding='utf-8').read())
    elif opcao_conta == '4':
        exec(open('contas/deletar.py', encoding='utf-8').read())
    elif opcao_conta == '0':
        break
    else:
        print("\nOpção inválida! Por favor, tente novamente.")
        
    input("\nPressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')