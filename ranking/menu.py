import os

while True:
    print("""
    --- MÓDULO DE RANKING ---
    [1] Ranking de Contas por Maiores Saldos
    [2] Ranking de Clientes por Nº de Transações
    [0] Voltar ao Menu Principal
    """)
    
    opcao = input("Escolha o ranking que deseja gerar => ")
    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao == '1':
        # Executa o seu arquivo de maiores saldos
        exec(open('ranking/maiores_saldos.py', encoding='utf-8').read())
    elif opcao == '2':
        # Executa o arquivo de ranking por transações (código abaixo)
        exec(open('ranking/ranking_clientes_transacoes.py', encoding='utf-8').read())
    elif opcao == '0':
        break
    else:
        print("\nOpção inválida!")
        
    input("\nPressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
