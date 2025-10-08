# dados.py
# Este arquivo define o "molde" ou a estrutura padrão e vazia do banco de dados.
# Ele é usado como um ponto de partida seguro caso o arquivo 'banco_de_dados.py'
# não seja encontrado.
# ESTE ARQUIVO NUNCA É MODIFICADO PELO PROGRAMA.

db = {
    # Módulo de Clientes
    "clientes": [],  # A lista de clientes começa vazia.
    "proximo_id_cliente": 1,

    # Módulo de Contas
    "contas": [],  # A lista de contas começa vazia.
    "proximo_id_conta": 1,

    # Módulo de Transações
    "transacoes": [],  # A lista de transações começa vazia.
    "proximo_id_transacao": 1,

    # Configurações Gerais do Sistema
    "config": {
        "taxa_rendimento_poupanca": 0.005,  # 0.5% ao mês
    }
}