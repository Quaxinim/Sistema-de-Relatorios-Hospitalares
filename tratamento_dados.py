import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import datetime


def importa_excel():
    # Importa a base de dados
    df = pd.read_excel("FaculdadeExcel.xlsx")
    return df


def tratamento_dados(df):
    # Tratamento de dados
    if df['horario'].isnull().sum() > 0 or df['genero'].isnull().sum() > 0 or df['especialidade'].isnull().sum() > 0:
        df.dropna(subset=['horario', 'genero', 'especialidade'], inplace=True)


# Importa os dados e trata.
df = importa_excel()
tratamento_dados(df)

# Trata o horario corretamente
df['horario'] = df['horario'].astype(str)
df['horario'] = pd.to_datetime(df['horario']).dt.strftime('%H:%M')

# Faz uma lista com nome das colunas que desejo e cria um novo df
lista_colunas = ['horario', 'genero', 'especialidade']
df_atendimentos = df[lista_colunas]
print((df_atendimentos))

# Inicia o dashboard
app = Dash(__name__)

fig = px.bar(df_atendimentos, x="especialidade",
                y="horario", color='genero', barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Dashboard de atendimentos'),
    html.Div(children='''
        Atendimentos por doutores
    '''),
    dcc.Dropdown(['Placeholder_1', 'Placeholder_2', 'Placeholder_3'],
                 'Placeholder_1', id='demo-dropdown'),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
