from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import exame_mais_usados
from functions import importa_excel, tratamento_dados
import pandas as pd

# Importa os dados e trata.
df = importa_excel()
tratamento_dados(df)

# Separa os generos
opcoes = list(df['genero'].unique())
opcoes.append("Todos os generos")

# Inicia o dashboard
app = Dash(__name__)

# Dataframes
df_exames = exame_mais_usados.df_sem_duplicacao
# Primeiro grafico (Quantidade de exames)
fig = px.bar(df_exames, x="especialidade", y="contagem", color='genero', barmode="group")

# Conta as repeticoes das palavras feminino e masculino na coluna genero
frequencias_genero = df['genero'].value_counts()
r_feminino = frequencias_genero['Feminino']
r_masculino = frequencias_genero['Masculino']

# Criando listas com seus dados
dados = [
    ["Feminino", r_feminino],
    ["Masculino", r_masculino],
]

# Criacao do dataframe com o dicionario
df_genero = pd.DataFrame(dados, columns=["Genero", "Quantidade de Exames"])

# Segundo grafico (Relacao Genero x Quantidade de atendimentos)
fig1 = px.bar(df_genero, x="Genero", y="Quantidade de Exames", color='Genero', barmode="group")


def iniciar_servidor():
    app.layout = html.Div(children=[
        html.H1(children='Dashboard de atendimentos'),
        html.H2(children='''
        Contagem de exames mais procurados:
        '''),
        html.Div(children='''
            OBS: Atenção ao preenchimento da planilha.
        '''),
        dcc.Graph(
            id='grafico_exames',
            figure=fig
        ),
        html.Div(children=[
            html.H2(children='Relação entre genero e quantidade de exames'),
            html.Div(children='''
            Abaixo tem a contagem de quantidade de exames feitos e a relação entre homems e mulheres
            '''),
        dcc.Graph(
            id='grafico_',
            figure=fig1
        )
        ])
    ]
    )

    if __name__ == '__main__':
        app.run(debug=True)


iniciar_servidor()