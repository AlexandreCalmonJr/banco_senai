# dados.py

# Dicionário principal que armazena todo o estado do banco em tempo de execução.
# Ele é inicializado com esta estrutura vazia e preenchido ao carregar o arquivo .json,
# ou populado com novos dados durante o uso do programa.
db = {
    # Módulo de Clientes
    "clientes": [],
    "proximo_id_cliente": 1,

    # Exemplo de como um dicionário de cliente é estruturado dentro da lista "clientes":
    # {
    #     'id_cliente': 1,
    #     'nome_cliente': 'Fulano de Tal',
    #     'idade_cliente': 30,
    #     'cpf_cliente': '12345678900',
    #     'tipo_cliente': 'PF',  # Pode ser 'PF' ou 'PJ'
    #     'sexo_cliente': 'Masculino'
    # }

    # Módulo de Contas
    "contas": [],
    "proximo_id_conta": 1,

    # Exemplo de como um dicionário de conta é estruturado dentro da lista "contas":
    # {
    #     'id_conta': 1,
    #     'id_cliente': 1,  # Chave que liga a conta ao seu respectivo cliente
    #     'tipo_conta': 'Poupança',  # Ex: Poupança, Corrente
    #     'saldo': 1500.50,
    #     'ativa': True  # Status da conta (pode ser ativada/desativada)
    # }

    # Módulo de Transações
    "transacoes": [],
    "proximo_id_transacao": 1,

    # Exemplo de como um dicionário de transação é estruturado dentro da lista "transacoes":
    # {
    #     'id_transacao': 1,
    #     'id_conta': 1,  # Chave que liga a transação à conta correspondente
    #     'tipo_trans': 'Depósito',  # Ex: Depósito, Saque, Rendimento
    #     'valor_trans': 500.00, # Valor positivo para entradas, negativo para saídas
    #     'data': '2025-10-05 16:30:00'
    # }

    # Configurações Gerais do Sistema
    "config": {
        "taxa_rendimento_poupanca": 0.005,  # 0.5% ao mês
    }
}