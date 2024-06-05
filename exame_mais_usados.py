import pandas as pd

df = pd.read_excel('FaculdadeExcel.xlsx')

exames = df['especialidade']


# Adiciona as duas colunas de nome do paciente e especialidade a um novo DF
df_paciente_atendimento = df.loc[:, ['nome do paciente', 'especialidade']]
# Remove a linha que contem um valor vazio na coluna "nome do paciente"
df_paciente_atendimento = df_paciente_atendimento.dropna(
    subset='nome do paciente')
# Remove as linhas 2 e 3 que estão com valores corrompidos
df_paciente_atendimento = df_paciente_atendimento.drop([1, 2])
# Contagem de exames mais feitos
contagem_exames = df_paciente_atendimento['especialidade'].value_counts()

# Cria e mistura as duas df, tira a coluna com nomes de pacientes e salva para uso posterior
df_especialidade_contagem = pd.DataFrame()
df_especialidade_contagem = df_paciente_atendimento.merge(
    contagem_exames.to_frame('contagem').reset_index(), on='especialidade')
df_especialidade_contagem = df_especialidade_contagem.drop(
    'nome do paciente', axis=1)
