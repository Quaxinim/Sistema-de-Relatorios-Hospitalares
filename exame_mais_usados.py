import pandas as pd
import tratamento_dados as td

df = td.importa_excel()
exames = df['especialidade']

# Adiciona as duas colunas de nome do paciente e especialidade a um novo DF
df_paciente_atendimento = df.loc[:, ['nome do paciente', 'especialidade']]
df_paciente_atendimento['especialidade'] = df['especialidade'].str.upper()

# Remove a linha que contem um valor vazio na coluna "nome do paciente"
df_paciente_atendimento = df_paciente_atendimento.dropna(
    subset='nome do paciente')

df_paciente_atendimento = df_paciente_atendimento.dropna(
    subset='especialidade')

# Contagem de exames mais feitos
contagem_exames = df_paciente_atendimento['especialidade'].value_counts()

# Cria e mistura as duas df, tira a coluna com nomes de pacientes e salva para uso posterior
df_especialidade_contagem = df_paciente_atendimento.merge(
    contagem_exames.to_frame('contagem').reset_index(), on='especialidade')
df_especialidade_contagem = df_especialidade_contagem.drop(
    'nome do paciente', axis=1)
# Removendo a duplicação de linhas na coluna especialidade
df_sem_duplicacao = df_especialidade_contagem.drop_duplicates(subset='especialidade', keep='first')

