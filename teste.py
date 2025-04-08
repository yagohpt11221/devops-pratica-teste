# Importa a função de cálculo e os dados de vendas do arquivo 'codigo.py'
from codigo import calcular_total_vendas, vendas_mensais

# Importa a biblioteca 'sys', que permite encerrar o programa com códigos de erro
# Isso é importante para o GitHub Actions identificar falhas
import sys

# Define uma função de teste para validar o total de vendas
def testar_total_vendas():
    resultado = calcular_total_vendas(vendas_mensais)  # Executa o cálculo com os dados atuais

    # Define os limites esperados para o total de vendas
    limite_minimo = 5000
    limite_maximo = 10000

    # Se o resultado estiver dentro da faixa, o teste passa
    if limite_minimo <= resultado <= limite_maximo:
        print("✅ Teste passou! Total de vendas dentro da faixa esperada.")
    else:
        # Se o resultado estiver fora da faixa, o teste falha
        print(f"❌ Teste falhou! Valor fora da faixa. Resultado obtido:", resultado)
        sys.exit(1)

# Executa a função de teste automaticamente ao rodar este arquivo
testar_total_vendas()
