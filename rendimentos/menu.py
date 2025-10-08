
import os

while True:
    print("""
    --- MÓDULO DE RENDIMENTOS ---
    [1] Aplicar Rendimento da Poupança (0.5%)
    [2] Simular Investimento com Juros Compostos
    [0] Voltar ao Menu Principal
    """)

    opcao = input("Escolha uma ação => ")
    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao == '1':
        exec(open('rendimentos/aplicar.py', encoding='utf-8').read())
    elif opcao == '2':
        # Crie um novo arquivo com este nome e o código abaixo
        exec(open('rendimentos/simular_composto.py', encoding='utf-8').read())
    elif opcao == '0':
        break
    else:
        print("\nOpção inválida!")

    input("\nPressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')