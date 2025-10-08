import os

while True:
    print("""
    --- MENU DE RELATÓRIOS ---
    [1] Relatório de Contas por Cliente
    [2] Relatório de Movimentações por Conta
    [0] Voltar ao Menu Principal
    """)
    
    opcao = input("Escolha o relatório que deseja gerar => ")
    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao == '1':
        exec(open('relatorios/clientes_e_contas.py', encoding='utf-8').read())
    elif opcao == '2':
        # Você precisará criar este arquivo. O código está abaixo.
        exec(open('relatorios/relatorio_movimentacoes.py', encoding='utf-8').read())
    elif opcao == '0':
        break
    else:
        print("\nOpção inválida!")
        
    input("\nPressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')