from dash import Dash, html, dcc, Input, Output, dash_table
import plotly.express as px
import exame_mais_usados
from functions import importa_excel, tratamento_dados
import pandas as pd

# Importa os dados e trata.
df = importa_excel()
tratamento_dados(df)

# Opcoes para o dropdown do dashboard, basta incluir o que deseja na lista.
opcoes = list(df['genero'].unique())
opcoes.append("Todos os generos")

# Dataframes
df_exames = exame_mais_usados.df_sem_duplicacao
opcoes_horarios = list(df['horario'].unique())

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

# Inicia o dashboard
app = Dash(__name__)

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
    ]),
    html.Div(children=[
        html.H2(children='Placeholder'),
        html.Div(children='''
    Place_holder
    '''),
        # Filtros
        dcc.Dropdown(
            id='dropdown-horario',
            options=[{'label': n, 'value': n} for n in df['horario'].unique()],
            value='Todos os horarios'),
        dcc.Dropdown(
            id='dropdown-nome-paciente',
            options=[{'label': n, 'value': n} for n in df['nome do paciente'].unique()],
            value='Todos os pacientes',
        ),
        # Datatable
        dash_table.DataTable(
            id='datatable',
            data=df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in df.columns])
    ])
])


@app.callback(
    Output('datatable', 'data'),
    [Input('dropdown-horario', 'value'),
     Input('dropdown-nome-paciente', 'value')
     # ... Adicione inputs para outros dropdowns aqui
     ]


)
def update_datatable(horario_selecionado, nome_paciente_selecionado):
    # Filtre o DataFrame com base nas seleções
    df_filtrado = df
    if horario_selecionado == 'Todos os horarios':
        df_filtrado = df_filtrado[df_filtrado['horario'] == horario_selecionado]
    if nome_paciente_selecionado != 'Todos os pacientes':
        df_filtrado = df_filtrado[df_filtrado['nome do paciente'] == nome_paciente_selecionado]
    # ... Adicione filtros para outros campos de filtro aqui
    # Retorne o DataFrame filtrado como dicionário de registros
    return df_filtrado.to_dict('records')


if __name__ == '__main__':
    app.run(debug=True)
