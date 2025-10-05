import sys
sys.path.append('..')
from dados import db

print("\n--- ATIVAR/DESATIVAR CONTA ---")
id_conta_str = input("Digite o ID da conta que deseja alterar o status: ")

conta_encontrada = None
try:
    id_conta = int(id_conta_str)
    for conta in db['contas']:
        if conta['id_conta'] == id_conta:
            conta_encontrada = conta
            break
except ValueError:
    print("ID inválido.")

if conta_encontrada:
    status_atual = "Ativa" if conta_encontrada['ativa'] else "Inativa"
    print(f"O status atual da conta {conta_encontrada['id_conta']} é: {status_atual}")
    
    confirmacao = input("Deseja inverter o status? (s/n): ").lower()
    if confirmacao == 's':
        conta_encontrada['ativa'] = not conta_encontrada['ativa']
        novo_status = "Ativa" if conta_encontrada['ativa'] else "Inativa"
        print(f"Status da conta alterado para: {novo_status}")
    else:
        print("Operação cancelada.")
else:
    print(f"Conta com ID {id_conta_str} não encontrada.")