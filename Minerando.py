# import pandas as pd
# import os
# import cufflinks as cf
# cf.go_offline()
# import plotly
# import plotly.offline as py
# import plotly.graph_objs as go
# from plotly.offline import plot, iplot
# import numpy as np
# import plotly.io as pio
# pio.renderers.default = "browser"
#
# plotly.offline.init_notebook_mode(connected=True)
# #
# #
# #
# os.chdir(r'C:\Users\paulo.roberto\Downloads\Visualizando Dados de Vendas Com Python\datasets')
# # os.chdir(r'C:\Users\paulo.roberto\Documents\Arquivos TXT')
#
# # razao = pd.read_csv('Realizado 2019 VP tecnica.txt', quoting=3, delimiter=';', skiprows=26, encoding='ANSI', thousands='.', decimal=',', low_memory=False, error_bad_lines=True)
# # df = razao[['Centro de Custo','Descrição Centro de Custo','Conta','Descrição Conta','Tipo de Servico','Descrição Tipo de Servico','Prefixo da Aeronave','Descrição Prefixo da Aeronave','Líquido','Mês','Data GL','Origem','Categoria','Histórico','Fornecedor','Numero NF RI/AP','Data NF RI/AP','Detalhe Historico RI/AP','Criador RI/AP','Comentarios da PO','Observacoes da Aprovacao PO','Conta Contrapartida']]
# # print(df['Data GL'])
#
# df = pd.read_csv(r'olist_classified_public_dataset.csv')
#
# df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'], errors='coerce')
# # print(df['order_purchase_timestamp'].dt.month)
# df['order_purchase_month'] = df.order_purchase_timestamp.dt.to_period('M').astype(str)
#
# vendas_por_mes = df.groupby(by='order_purchase_month').order_products_value.sum()
#
#
#
# data = [go.Bar(x=vendas_por_mes.index,
#                y=vendas_por_mes.values,
#                marker = {'color': 'lightblue'})]
#
# # Criando Layout
# configuracoes_layout = go.Layout(title='Vendas no Periodo',
#                                  yaxis={'title':'Valores em Vendas'},
#                                  xaxis={'title': 'Periodo'})
#
# # Objeto figura
#
# fig = go.Figure(data=data, layout=configuracoes_layout)
#
# # plotando o grafico
# py.iplot(fig)
# fig.show()
#
# # import plotly.graph_objects as go
# # fig = go.Figure( go.Scatter(x=[1,2,3], y=[1,3,2] ) )
# # fig.show()
#
#
# import plotly.graph_objects as go
# import plotly.io as pio
# 
# pio.renderers.default = 'png'
# 
# fig = go.Figure(
#     data=[go.Bar(y=[2, 1, 3])],
#     layout_title_text="A Figure Displayed with fig.show()"
# )
# fig.show()
#
# import cufflinks as cf
# from plotly.offline import iplot
# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame(np.random.randn(100,4), columns=['A','B','C','D'])
# cf.go_offline()
#
# df.sum().iplot(kind='bar', title='Gráfico de barras')
# import pandas as pd
# import plotly.graph_objects as go
#
# # importar os dados do BBAS3 csv->dataframe
# df = pd.read_csv(
#     "https://raw.githubusercontent.com/carlosfab/curso_data_science_na_pratica/master/modulo_02/BBAS3.SA.csv")
#
# # criar um gráfico interativo com o Plotly
#
# # gráfico bbas3 (candlestick
# trace1 = {
#     'x': df.Date,
#     'open': df.Open,
#     'close': df.Close,
#     'high': df.High,
#     'low': df.Low,
#     'type': 'candlestick',
#     'name': 'BBAS3',
#     'showlegend': False
# }
#
# # informar todos os dados e gráficos em uma lista
# data = [trace1]
#
# # configurar o layout do gráfico
# layout = go.Layout({
#     'title': {
#         'text': 'Gráfico de Candlestick - BBAS3',
#         'font': {
#             'size': 20
#         }
#     }
# })
#
# # instanciar objeto Figure e plotar o gráfico
# fig = go.Figure(data=data, layout=layout)
# fig.show()
#
# import win32com.client
#
# xlapp = win32com.client.DispatchEx("Excel.Application")
#
# wb = xlapp.workbooks.open(r"//azul.corp/arquivos/Corporativo/Diretoria Tecnica/1-Gestão de Custos/Indicadores-Analise/Requisições Heavy Check/Relatorio preço itens.xlsx")
#
# wb.RefreshAll()
# wb.Save()
#
# xlapp.Quit()
import os
import pandas as pd
import pprint as pp

os.chdir(r'R:/Corporativo/Diretoria Tecnica/1-Gestão de Custos/Budget/Orçamento 2020/Recebido Gestores/Arquivos/Budget Final Area')

# for file in os.listdir():
    # df = pd.read_excel(file,skiprows=4,header=True)

df = pd.read_excel('2300 - Resposta a emergencia.xlsx', skiprows=4)
df = df.fillna(0)
df = df[df['Conta'] != 0]
print(df.head())
