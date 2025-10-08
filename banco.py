# banco.py
# Este é o arquivo principal e o coração do sistema.
# Ele controla o menu principal, carrega os dados na inicialização e os salva ao sair.

import os
import pprint
import datetime  # Importado para obter a data atual
import dados

# --- LÓGICA DE CARREGAMENTO DOS DADOS ---
try:
    from banco_de_dados import db as db_salvo
    dados.db = db_salvo
    print("Dados do banco carregados com sucesso!")
except ImportError:
    print("Arquivo 'banco_de_dados.py' não encontrado. Iniciando com base de dados vazia.")

# --- MENSAGEM DE BOAS-VINDAS ---
print("\n======================================")
print("   BEM-VINDO AO BANCO SENAI")
# Adiciona a data atual de forma dinâmica
print(f"   {datetime.date.today().strftime('%d de %B de %Y')}")
print("======================================")
print("Em que podemos te ajudar hoje?\n")


while True:
    print("""
    --- MENU PRINCIPAL ---
    [1] Clientes
    [2] Contas
    [3] Transações Financeiras
    [4] Rendimentos
    [5] Relatórios
    [6] Ranking do Banco
    [0] Sair do Sistema e Salvar
    """)
    
    opcao_principal = input("Escolha o módulo desejado => ")
    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao_principal == '1':
        exec(open('clientes/menu.py', encoding='utf-8').read())
    elif opcao_principal == '2':
        exec(open('contas/menu.py', encoding='utf-8').read())
    elif opcao_principal == '3':
        exec(open('transacoes/menu.py', encoding='utf-8').read())
    elif opcao_principal == '4':
        exec(open('relatorios/menu.py', encoding='utf-8').read())
    elif opcao_principal == '5':
        exec(open('ranking/menu.py', encoding='utf-8').read())
    elif opcao_principal == '6':
        exec(open('rendimentos/menu.py', encoding='utf-8').read())
    elif opcao_principal == '0':
        # --- LÓGICA DE SALVAMENTO ---
        try:
            with open('banco_de_dados.py', 'w', encoding='utf-8') as f:
                # Converte o dicionário 'db' para uma string formatada
                conteudo_formatado = pprint.pformat(dados.db)
                # Escreve a string no arquivo, no formato de uma variável Python
                f.write(f"db = {conteudo_formatado}\n")
            print("\nDados salvos com sucesso!")
        except Exception as e:
            print(f"\nOcorreu um erro ao salvar os dados: {e}")
        break  
        print("\nOpção inválida! Por favor, escolha uma opção do menu.")
    
    input("\nPressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
