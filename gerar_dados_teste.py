import pandas as pd

def criar_cenario_teste():
    print("🛠️ Criando arquivos de teste para a Auditoria...")

    # Dados de Vendas (Simulando o que saiu do sistema de vendas)
    # Coloquei alguns IDs que vão dar erro de propósito para testar o Alerta
    dados_vendas = {
        'produto_id': [1001, 1002, 1003, 1004, 1005, 1006],
        'quantidade_vendida': [45, 12, 80, 25, 10, 55]
    }

    # Dados de Estoque (Simulando o que tem no galpão físico)
    dados_estoque = {
        'produto_id': [1001, 1002, 1003, 1004, 1005, 1006],
        'quantidade_estoque': [50, 15, 30, 22, 100, 40]
    }

    # Gerando os CSVs
    pd.DataFrame(dados_vendas).to_csv('vendas.csv', index=False)
    pd.DataFrame(dados_estoque).to_csv('estoque.csv', index=False)

    print("✅ Arquivos 'vendas.csv' e 'estoque.csv' criados com sucesso na sua pasta!")
    print("🚀 Agora você já pode rodar o script principal do Dashboard.")

if __name__ == "__main__":
    criar_cenario_teste()