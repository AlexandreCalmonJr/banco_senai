# Arquivo: dados.py
# dados.py

# Dicionário principal que armazena todo o estado do banco em tempo de execução.
# Ele é inicializado vazio e preenchido ao carregar o arquivo .json,
# ou preenchido com novos dados durante o uso do programa.
db = {
    # Módulo de Clientes
    "clientes": [],
    "proximo_id_cliente": 1,

    # Exemplo de como um dicionário de cliente é estruturado:
    # {
    #     'id_cliente': 1,
    #     'nome_cliente': 'João da Silva',
    #     'idade_cliente': 35,
    #     'cpf_cliente': '12345678900',
    #     'tipo_cliente': 'PF',  # Pode ser 'PF' ou 'PJ'
    #     'sexo_cliente': 'Masculino'
    # }

    # Módulo de Contas
    "contas": [],
    "proximo_id_conta": 1,

    # Exemplo de como um dicionário de conta é estruturado:
    # {
    #     'id_conta': 1,
    #     'id_cliente': 1,  # Chave que liga a conta ao cliente
    #     'tipo_conta': 'Poupança',  # Ex: Poupança, Corrente
    #     'saldo': 2500.75,
    #     'ativa': True  # Para ativar ou desativar a conta
    # }

    # Módulo de Transações
    "transacoes": [],
    "proximo_id_transacao": 1,

    # Exemplo de como um dicionário de transação é estruturado:
    # {
    #     'id_transacao': 1,
    #     'id_conta': 1,  # Chave que liga a transação à conta
    #     'tipo_trans': 'Depósito',  # Ex: Depósito, Saque, Rendimento
    #     'valor_trans': 500.00,
    #     'data': '2025-10-03 23:30:00'
    # }

    # Configurações Gerais do Sistema
    "config": {
        "taxa_rendimento_poupanca": 0.005,  # 0.5% ao mês
    }
}