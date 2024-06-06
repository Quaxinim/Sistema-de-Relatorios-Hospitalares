import pandas as pd
import tratamento_dados as td

# Importa a base de dados
df = td.importa_excel()

# Tratamento de dados (
if df['genero'].isnull().sum() > 0 or df['medico'].isnull().sum() > 0 or df['especialidade'].isnull().sum() > 0:
    df.dropna(subset=['genero', 'medico', 'especialidade'], inplace=True)


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
df_contagem_medicos = pd.DataFrame(columns=['medico', 'contagem'])

# Percorra a lista de médicos e conta quantos atendimentos tiveram associados a cada nome unico da lista.
for medico in medicos:
    numero_atendimentos = contagem_total_atendimento_doutor(medico)
    # Cria um DataFrame temporário com as informações do médico atual
    df_medico = pd.DataFrame(
        {'medico': [medico], 'contagem': [numero_atendimentos]})
    # Concatena o DataFrame temporário com o DataFrame principal
    df_contagem_medicos = pd.concat(
        [df_contagem_medicos, df_medico, ], ignore_index=True)

print(df_contagem_medicos)

