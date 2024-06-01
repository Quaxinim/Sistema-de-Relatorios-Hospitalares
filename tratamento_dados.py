import pandas as pd

# Importa a base de dados
df = pd.read_excel("FaculdadeExcel.xlsx")

# Verificando a quantidade de linhas com valores nulos e
# Excluindo linhas com valores nulos nas colunas relevantes (se necessário)
if df['genero'].isnull().sum() > 0 or df['medico'].isnull().sum() > 0:
    df.dropna(subset=['genero', 'medico'], inplace=True)


def contagem_masc_fem_doutor(genero_pacie, nome_doutor):
    """
    Função para contar o número de pacientes por gênero atendidos por um médico específico.

    Argumentos:
        genero_pacie (str): Gênero do paciente ("Masculino" ou "Feminino").
        nome_doutor (str): Nome do médico a ser pesquisado.

    Retorna:
        int: Quantidade de pacientes do gênero especificado atendidos pelo médico.
    """

    try:
        # Validando valores de entrada
        if genero_pacie not in ['Masculino', 'Feminino']:
            raise ValueError(f"Gênero inválido: {genero_pacie}")
        if nome_doutor not in df['medico'].unique():
            raise ValueError(f"Nome do médico inválido: {nome_doutor}")

        # Filtrando dados
        pacientes_filtrados = df[(df['genero'] == genero_pacie) & (df['medico'] == nome_doutor)]
        print(pacientes_filtrados)

        # Contando pacientes
        numero_pacientes = pacientes_filtrados.shape[0]

        # Retornando resultado
        return numero_pacientes

    except ValueError as e:
        print(f"Erro: {e}")
        return None



