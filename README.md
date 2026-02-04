# 📊 Auditoria de Estoque Inteligente com Python

Este projeto foi desenvolvido para automatizar o processo de auditoria de estoque, cruzando dados de vendas e estoque físico. Ele gera um dashboard profissional em Excel com alertas visuais e gráficos automáticos.

## 🚀 O que este projeto faz?
- **Integração de Dados**: Lê arquivos CSV e faz o cruzamento de informações usando a biblioteca Pandas.
- **Lógica de Auditoria**: Identifica automaticamente onde a venda superou o estoque (ruptura).
- **Relatório Profissional**: Gera um arquivo `.xlsx` com:
  - Formatação condicional (células vermelhas para alertas).
  - Gráfico de barras nativo comparando Vendas vs Estoque.
  - Cabeçalhos estilizados.

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Pandas**: Para manipulação e tratamento de dados.
- **XlsxWriter**: Para criação e estilização do Dashboard em Excel.

## 📦 Como Executar o Projeto
1. Instale as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt