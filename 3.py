import json

# Carrega os dados do faturamento mensal a partir do arquivo JSON
with open('faturamento.json') as f:
    faturamento_mensal = json.load(f)

# Calcula a média mensal de faturamento, ignorando dias sem faturamento
dias_com_faturamento = [dia for dia in faturamento_mensal if dia['valor'] > 0]
media_mensal = sum(dia['valor'] for dia in dias_com_faturamento) / len(dias_com_faturamento)

# Calcula o menor valor de faturamento ocorrido em um dia do mês
menor_valor = min(dia['valor'] for dia in faturamento_mensal)

# Calcula o maior valor de faturamento ocorrido em um dia do mês
maior_valor = max(dia['valor'] for dia in faturamento_mensal)

# Calcula o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = len([dia for dia in faturamento_mensal if dia['valor'] > media_mensal])

# Exibe os resultados
print(f"Menor valor: R${menor_valor:.2f}")
print(f"Maior valor: R${maior_valor:.2f}")
print(f"Dias acima da média: {dias_acima_da_media}")
