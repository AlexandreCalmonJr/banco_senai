# Menu principal do sistema.

import os

# Carrega os dados (variáveis: clientes, contas, transacoes)


print("======================================")
print("   BEM-VINDO AO BANCO SENAI")
print("======================================")
print("Em que podemos te ajudar hoje?\n")


while True:
    print("""
    --- MENU PRINCIPAL ---
    [1] Cliente do Banco
    [2] Contas do Banco
    [3] Transação Financeira
    [4] Rendimentos
    [5] Relatórios
    [6] Ranking do Banco
    [0] Sair do Sistema
    """)
    
    opcao_principal = input("Escolha o módulo desejado => ")

    if opcao_principal == '1':
        # Executa o menu que está dentro da pasta 'clientes'
        exec(open('clientes/menu.py', encoding='utf-8').read())
    elif opcao_principal == '2':
        # Executa o menu que está dentro da pasta 'contas'
        exec(open('contas/menu.py', encoding='utf-8').read())
    elif opcao_principal == '3':
        exec(open('transacoes/menu.py', encoding='utf-8').read())
    elif opcao_principal == '4':
        exec(open('rendimentos/menu.py', encoding='utf-8').read())
    elif opcao_principal == '5':
        exec(open('relatorios/menu.py', encoding='utf-8').read())
    elif opcao_principal == '6':
        exec(open('ranking/menu.py', encoding='utf-8').read())
    elif opcao_principal == '0':
        print("\nObrigado por utilizar o Banco SENAI. Até logo!")
        break
    else:
        print("\nOpção inválida! Por favor, escolha uma opção do menu.")
    
    input("\nPressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
