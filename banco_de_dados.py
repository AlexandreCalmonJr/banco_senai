db = {
    # === CLIENTES ===
    "clientes": [
        {'id_cliente': 1, 'nome_cliente': 'Mariana Lima Santos', 'idade_cliente': 34, 'cpf_cliente': '12345678901', 'tipo_cliente': 'PF', 'sexo_cliente': 'Feminino'},
        {'id_cliente': 2, 'nome_cliente': 'TecnoSoluções Ltda', 'idade_cliente': 8, 'cpf_cliente': '01234567000188', 'tipo_cliente': 'PJ', 'sexo_cliente': 'N/A'},
        {'id_cliente': 3, 'nome_cliente': 'Ricardo Almeida', 'idade_cliente': 52, 'cpf_cliente': '98765432109', 'tipo_cliente': 'PF', 'sexo_cliente': 'Masculino'},
        {'id_cliente': 4, 'nome_cliente': 'Fernanda Costa', 'idade_cliente': 25, 'cpf_cliente': '11223344556', 'tipo_cliente': 'PF', 'sexo_cliente': 'Feminino'},
        {'id_cliente': 5, 'nome_cliente': 'ConstruForte Engenharia', 'idade_cliente': 15, 'cpf_cliente': '88776655000144', 'tipo_cliente': 'PJ', 'sexo_cliente': 'N/A'},
        {'id_cliente': 6, 'nome_cliente': 'Lucas Pereira', 'idade_cliente': 41, 'cpf_cliente': '66554433221', 'tipo_cliente': 'PF', 'sexo_cliente': 'Masculino'}
    ],
    "proximo_id_cliente": 7,

    # === CONTAS ===
    "contas": [
        {'id_conta': 1, 'id_cliente': 1, 'tipo_conta': 'Corrente', 'saldo': 3450.60, 'ativa': True},
        {'id_conta': 2, 'id_cliente': 1, 'tipo_conta': 'Poupança', 'saldo': 25800.00, 'ativa': True},
        {'id_conta': 3, 'id_cliente': 2, 'tipo_conta': 'Corrente', 'saldo': 115234.98, 'ativa': True},
        {'id_conta': 4, 'id_cliente': 3, 'tipo_conta': 'Poupança', 'saldo': 189500.55, 'ativa': True},
        {'id_conta': 5, 'id_cliente': 4, 'tipo_conta': 'Corrente', 'saldo': 890.10, 'ativa': True},
        {'id_conta': 6, 'id_cliente': 5, 'tipo_conta': 'Corrente', 'saldo': 0.00, 'ativa': True},
        {'id_conta': 7, 'id_cliente': 6, 'tipo_conta': 'Corrente', 'saldo': -50.25, 'ativa': False},
    ],
    "proximo_id_conta": 8,

    # === TRANSAÇÕES ===
    "transacoes": [
        {'id_transacao': 1, 'id_conta': 1, 'tipo_trans': 'Depósito', 'valor_trans': 3500.00, 'data': '2025-09-10 10:22:05'},
        {'id_transacao': 2, 'id_conta': 1, 'tipo_trans': 'Saque', 'valor_trans': -49.40, 'data': '2025-09-12 15:05:11'},
        {'id_transacao': 3, 'id_conta': 2, 'tipo_trans': 'Depósito', 'valor_trans': 25800.00, 'data': '2025-09-01 11:00:00'},
        {'id_transacao': 4, 'id_conta': 3, 'tipo_trans': 'Depósito', 'valor_trans': 200000.00, 'data': '2025-09-28 18:30:00'},
        {'id_transacao': 5, 'id_conta': 3, 'tipo_trans': 'Saque', 'valor_trans': -84765.02, 'data': '2025-10-02 09:12:45'},
        {'id_transacao': 6, 'id_conta': 4, 'tipo_trans': 'Depósito', 'valor_trans': 189500.55, 'data': '2025-08-20 16:00:01'},
        {'id_transacao': 7, 'id_conta': 5, 'tipo_trans': 'Depósito', 'valor_trans': 1000.00, 'data': '2025-10-01 14:21:33'},
        {'id_transacao': 8, 'id_conta': 5, 'tipo_trans': 'Saque', 'valor_trans': -109.90, 'data': '2025-10-03 19:55:00'},
        {'id_transacao': 9, 'id_conta': 7, 'tipo_trans': 'Saque', 'valor_trans': -50.25, 'data': '2025-09-30 20:10:10'},
        {'id_transacao': 10, 'id_conta': 2, 'tipo_trans': 'Rendimento', 'valor_trans': 129.00, 'data': '2025-10-01 00:00:00'},
        {'id_transacao': 11, 'id_conta': 4, 'tipo_trans': 'Rendimento', 'valor_trans': 947.50, 'data': '2025-09-01 00:00:00'}
    ],
    "proximo_id_transacao": 12,

    # === CONFIGURAÇÕES ===
    "config": {
        "taxa_rendimento_poupanca": 0.005,
    }
}
