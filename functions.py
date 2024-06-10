import pandas as pd


def importa_excel():
    # Importa a base de dados
    df = pd.read_excel("FaculdadeExcel.xlsx")
    return df


def tratamento_dados(df):
    # Tratamento de dados
    if df['horario'].isnull().sum() > 0 or df['genero'].isnull().sum() > 0 or df['especialidade'].isnull().sum() > 0:
        df.dropna(subset=['horario', 'genero', 'especialidade'], inplace=True)
