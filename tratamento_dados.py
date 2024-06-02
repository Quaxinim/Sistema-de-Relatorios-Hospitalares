import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Importa a base de dados
df = pd.read_excel("FaculdadeExcel.xlsx")
print(df)
# Verificando a quantidade de linhas com valores nulos e
# Excluindo linhas com valores nulos nas colunas relevantes (se necessário)

df_novo = df.loc[:, ['medico', 'especialidade']]
print(df_novo)

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

app = Dash(__name__)

fig = px.bar(df_novo, x="medico", y="especialidade", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
