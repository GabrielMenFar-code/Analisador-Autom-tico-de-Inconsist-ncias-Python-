import pandas as pd
from datetime import datetime

# Essa função faz o Excel ficar com cara de software profissional
def gerar_dashboard_luxo(arquivo_vendas, arquivo_estoque):
    print(f"--- 🚀 Iniciando Processamento: {datetime.now().strftime('%H:%M:%S')} ---")

    try:
        # 1. CARREGANDO OS DADOS
        # O Pandas lê os arquivos que o seu outro script gerou
        df_vendas = pd.read_csv(arquivo_vendas)
        df_estoque = pd.read_csv(arquivo_estoque)

        # 2. CRUZANDO OS DADOS (PROCV inteligente)
        # O inner join garante que só vamos analisar produtos que existem nas duas listas
        relatorio = pd.merge(df_vendas, df_estoque, on='produto_id', how='inner')

        # 3. LÓGICA DE NEGÓCIO (Onde o humano falha e o Python brilha)
        relatorio['Status'] = relatorio.apply(
            lambda x: 'ALERTA' if x['quantidade_vendida'] > x['quantidade_estoque'] else 'NORMAL', axis=1
        )
        relatorio['Diferença'] = relatorio['quantidade_estoque'] - relatorio['quantidade_vendida']

        # 4. CONFIGURANDO O EXCEL COM XLSXWRITER
        nome_arquivo = 'Dashboard_Auditoria_Tech.xlsx'
        writer = pd.ExcelWriter(nome_arquivo, engine='xlsxwriter')
        relatorio.to_excel(writer, sheet_name='Auditoria', index=False)

        workbook  = writer.book
        worksheet = writer.sheets['Auditoria']

        # 5. ESTILIZAÇÃO DO CABEÇALHO (Azul escuro com letra branca)
        header_format = workbook.add_format({
            'bold': True, 'text_wrap': True, 'valign': 'top',
            'fg_color': '#1F4E78', 'font_color': 'white', 'border': 1
        })

        for col_num, value in enumerate(relatorio.columns.values):
            worksheet.write(0, col_num, value, header_format)

        # 6. FORMATAÇÃO CONDICIONAL (Fica vermelho se for ALERTA)
        red_format = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
        worksheet.conditional_format('C2:C100', {
            'type':     'cell',
            'criteria': 'equal to',
            'value':    '"ALERTA"',
            'format':   red_format
        })

        # 7. CRIANDO O GRÁFICO DE BARRAS DENTRO DO EXCEL
        chart = workbook.add_chart({'type': 'column'})

        # Série de Vendas
        chart.add_series({
            'name':       'Qtd Vendida',
            'categories': ['Auditoria', 1, 0, len(relatorio), 0],
            'values':     ['Auditoria', 1, 1, len(relatorio), 1],
            'fill':       {'color': '#4472C4'},
        })
        
        # Série de Estoque
        chart.add_series({
            'name':       'Qtd em Estoque',
            'values':     ['Auditoria', 1, 2, len(relatorio), 2],
            'fill':       {'color': '#ED7D31'},
        })

        chart.set_title({'name': 'Análise de Ruptura de Estoque (Real vs Necessário)'})
        chart.set_x_axis({'name': 'ID do Produto'})
        chart.set_y_axis({'name': 'Unidades'})

        # Inserindo o gráfico na posição G2
        worksheet.insert_chart('G2', chart)

        writer.close()
        print(f"✅ Dashboard '{nome_arquivo}' gerado com sucesso!")
        print("💡 Abra o arquivo Excel para ver o resultado final.")

    except Exception as e:
        print(f"❌ Erro fatal: {e}")

# CHAMADA DA FUNÇÃO
if __name__ == "__main__":
    gerar_dashboard_luxo('vendas.csv', 'estoque.csv')