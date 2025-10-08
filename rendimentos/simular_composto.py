

print("\n--- SIMULADOR DE INVESTIMENTO (JUROS COMPOSTOS) ---")
print("Simule investimentos como CDI, CDB, LCI, etc.")

try:
    valor_inicial_str = input("Digite o valor inicial do investimento (ex: 1000.00): ")
    taxa_mensal_str = input("Digite a taxa de juros mensal (ex: para 1% digite 1): ")
    tempo_meses_str = input("Digite o tempo em meses (ex: 12): ")

    valor_inicial = float(valor_inicial_str)
    taxa_mensal = float(taxa_mensal_str) / 100  # Converte 1 para 0.01
    tempo_meses = int(tempo_meses_str)

    if valor_inicial <= 0 or taxa_mensal <= 0 or tempo_meses <= 0:
        print("\nErro: Todos os valores devem ser positivos.")
    else:
        # Fórmula dos juros compostos: M = C * (1 + i)^t
        montante_final = valor_inicial * ((1 + taxa_mensal) ** tempo_meses)
        total_juros = montante_final - valor_inicial

        print("\n" + "="*30)
        print("      RESULTADO DA SIMULAÇÃO")
        print("="*30)
        print(f"Valor Investido: R$ {valor_inicial:.2f}")
        print(f"Taxa Mensal: {taxa_mensal*100:.2f}%")
        print(f"Período: {tempo_meses} meses")
        print("-" * 30)
        print(f"Total em Juros: R$ {total_juros:.2f}")
        print(f"Montante Final: R$ {montante_final:.2f}")
        print("="*30)

except ValueError:
    print("\nErro: Por favor, digite valores numéricos válidos.")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")