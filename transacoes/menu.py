import os
while True:
    print("""
    --- TRANSAÇÕES FINANCEIRAS ---
    [1] Depositar
    [2] Sacar
    [3] Ver Extrato da Conta
    [0] Voltar ao Menu Principal
    """)
    opcao = input("Escolha uma ação => ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if opcao == '1': exec(open('transacoes/depositar.py', encoding='utf-8').read())
    elif opcao == '2': exec(open('transacoes/sacar.py', encoding='utf-8').read())
    elif opcao == '3': exec(open('transacoes/extrato.py', encoding='utf-8').read())
    elif opcao == '0': break
    else: print("\nOpção inválida!")
    input("\nPressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')