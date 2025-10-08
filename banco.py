# banco.py
# Este é o coração do sistema. Ele gerencia o menu principal,
# carrega os dados ao iniciar e salva ao finalizar.

import os
import pprint
import dados
from datetime import datetime

# --- LÓGICA DE CARREGAMENTO E SALVAMENTO ---
try:
    # Tenta importar os dados salvos do 'banco_de_dados.py'
    from banco_de_dados import db as db_salvo
    dados.db = db_salvo
    print("Dados do banco carregados com sucesso!")
except ImportError:
    # Se não encontrar, usa o 'molde' vazio do 'dados.py'
    print("Arquivo 'banco_de_dados.py' não encontrado. Iniciando com base de dados vazia.")

# Pega a data atual para exibir no cabeçalho
data_atual = datetime.now().strftime("%d de %B de %Y")

print("\n======================================")
print("   BEM-VINDO AO BANCO SENAI")
print(f"   Salvador, Bahia - {data_atual}")
print("======================================")

while True:
    print("""
    --- MENU PRINCIPAL ---
    [1] Clientes
    [2] Contas
    [3] Transações Financeiras
    [4] Relatórios
    [5] Ranking
    [6] Rendimentos
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
        try:
            with open('banco_de_dados.py', 'w', encoding='utf-8') as f:
                conteudo_formatado = pprint.pformat(dados.db)
                f.write(f"db = {conteudo_formatado}\n")
            print("\nDados salvos com sucesso em 'banco_de_dados.py'!")
        except Exception as e:
            print(f"\nOcorreu um erro ao salvar os dados: {e}")
        break
    else:
        print("\nOpção inválida! Por favor, escolha uma opção do menu.")
    
    input("\nPressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

