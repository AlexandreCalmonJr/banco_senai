import sys
sys.path.append('..')
from dados import db

print("\n--- DELETAR CONTA ---")
id_conta_str = input("Digite o ID da conta que deseja deletar: ")

conta_encontrada = None
try:
    id_conta = int(id_conta_str)
    for conta in db['contas']:
        if conta['id_conta'] == id_conta:
            conta_encontrada = conta
            break
except ValueError:
    print("ID inválido.")

if not conta_encontrada:
    print(f"Conta com ID {id_conta_str} não encontrada.")
elif conta_encontrada['saldo'] != 0:
    print(f"ERRO: Não é possível deletar a conta. O saldo precisa ser R$ 0,00. Saldo atual: R$ {conta_encontrada['saldo']:.2f}")
else:
    confirmacao = input(f"A conta {conta_encontrada['id_conta']} tem saldo zero. Tem certeza que deseja deletá-la? (s/n): ").lower()
    if confirmacao == 's':
        db['contas'].remove(conta_encontrada)
        print("Conta deletada com sucesso!")
    else:
        print("Operação cancelada.")