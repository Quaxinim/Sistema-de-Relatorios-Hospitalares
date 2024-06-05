import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import exame_mais_usados

# Importa a base de dados
df = pd.read_excel("FaculdadeExcel.xlsx")

# Tratamento de dados
if df['genero'].isnull().sum() > 0 or df['medico'].isnull().sum() > 0:
    df.dropna(subset=['genero', 'medico'], inplace=True)


# Função de contagem de atendimentos
def contagem_total_atendimento_doutor(nome_doutor, genero_pacie=None):
    # Validando valor de entrada
    if nome_doutor not in df['medico'].unique():
        raise ValueError(f"Nome do médico inválido: {nome_doutor}")
    # Filtrando dados por médico (gênero opcional)
    if genero_pacie is None:
        pacientes_filtrados = df[df['medico'] == nome_doutor]
    else:
        pacientes_filtrados = df[(df['genero'] == genero_pacie) & (
            df['medico'] == nome_doutor)]

    # Contando atendimentos
    numero_atendimentos = pacientes_filtrados.shape[0]

    # Retornando resultado
    return numero_atendimentos


# Cria um dataframe com os medicos e remove as duplicatas e conta os medicos
medicos = df['medico'].drop_duplicates()
contagem_por_medico = {}

# Cria um dataframe para o futuro armazenamento dos nomes dos medicos e das contagens de atendiementos
df_contagem_medicos = pd.DataFrame(columns=['medicos', 'contagem_por_medico'])

# Percorra a lista de médicos e conta quantos atendimentos tiveram associados a cada nome unico da lista.
for medico in medicos:
    numero_atendimentos = contagem_total_atendimento_doutor(medico)
    # Cria um DataFrame temporário com as informações do médico atual
    df_medico = pd.DataFrame(
        {'medico': [medico], 'contagem_por_medico': [numero_atendimentos]})
    # Concatena o DataFrame temporário com o DataFrame principal
    df_contagem_medicos = pd.concat(
        [df_contagem_medicos, df_medico], ignore_index=True)

# Inicia o dashboard
app = Dash(__name__)

fig = px.bar(df_contagem_medicos, x="medico",
             y="contagem_por_medico", barmode="group")

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
