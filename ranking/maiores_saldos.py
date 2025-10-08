# Exibir o ranking das contas com os maiores saldos,

print("\n=== RANKING: CONTAS COM MAIORES SALDOS ===")

# Pergunta quantos resultados o usuário quer ver
limite_txt = input("Quantos primeiros colocados deseja visualizar? (Enter = 5): ").strip()

# Verificação manual se é número inteiro
eh_numero = True
if limite_txt == "":
    eh_numero = False
else:
    i = 0
    while i < len(limite_txt):
        ch = limite_txt[i]
        # se tiver qualquer caractere que não seja dígito, marca como falso
        if ch < '0' or ch > '9':
            eh_numero = False
            break
        i = i + 1

if eh_numero:
    limite = int(limite_txt)
else:
    limite = 5  # valor padrão

# Caso não haja contas cadastradas
if len(contas) == 0:
    print("Nenhuma conta encontrada no sistema.")
else:
    # Cria uma cópia dos IDs das contas para controle
    ids_restantes = []
    for c in contas:
        ids_restantes.append(c["id_conta"])

    posicao = 1  # contador de posição no ranking

    # Enquanto ainda houver contas e não atingimos o limite pedido
    while len(ids_restantes) > 0 and posicao <= limite:
        # Busca o maior saldo entre as contas restantes
        maior_id = None
        maior_saldo = None

        # Percorre as contas restantes para encontrar a de maior saldo
        for id_conta in ids_restantes:
            for c in contas:
                if c["id_conta"] == id_conta:
                    saldo_atual = c["saldo"]

                    # Se for a primeira ou tiver saldo maior, guarda
                    if maior_saldo is None or saldo_atual > maior_saldo:
                        maior_saldo = saldo_atual
                        maior_id = id_conta
                    break  # já achou a conta correspondente; sai do laço interno

        # Após achar o maior saldo, exibe as informações
        if maior_id is not None:
            # Busca os dados da conta e do cliente dono dela
            nome_cliente = "Desconhecido"
            tipo_conta = ""
            for conta in contas:
                if conta["id_conta"] == maior_id:
                    tipo_conta = conta["tipo_conta"]
                    id_cliente = conta["id_cliente"]
                    # Procura o cliente correspondente
                    for cli in clientes:
                        if cli["id_cliente"] == id_cliente:
                            nome_cliente = cli["nome_cliente"]
                            break
                    break

            # Exibição do ranking
            print("-------------------------------------")
            print("Posição:", posicao)
            print("Cliente:", nome_cliente)
            print("Tipo de Conta:", tipo_conta)
            print("ID da Conta:", maior_id)
            print("Saldo: R$", round(maior_saldo, 2))

            # Remove essa conta da lista de IDs restantes
            nova_lista = []
            for x in ids_restantes:
                if x != maior_id:
                    nova_lista.append(x)
            ids_restantes = nova_lista

            # Incrementa posição
            posicao = posicao + 1
        else:
            # Caso não haja mais contas válidas
            break

    print("-------------------------------------")
    print("Ranking exibido com sucesso!")