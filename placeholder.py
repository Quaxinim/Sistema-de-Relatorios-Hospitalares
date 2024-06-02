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


def contagem_total_atendimento_doutor(nome_doutor, genero_pacie=None):
    # Validando valor de entrada
    if nome_doutor not in df['medico'].unique():
        raise ValueError(f"Nome do médico inválido: {nome_doutor}")
    # Filtrando dados por médico (gênero opcional)
    if genero_pacie is None:
        pacientes_filtrados = df[df['medico'] == nome_doutor]
    else:
        pacientes_filtrados = df[(df['genero'] == genero_pacie) & (df['medico'] == nome_doutor)]

    # Contando atendimentos
    numero_atendimentos = pacientes_filtrados.shape[0]

    # Retornando resultado
    return numero_atendimentos


# Contando o tamanho da coluna medicos e rodando a função "contagem


# Cria um dataframe com os medicos e remove as duplicatas e conta os medicos
medicos = df['medico'].drop_duplicates()
contagem_por_medico = {}

# Percorra a lista de médicos
for medico in medicos:
    numero_atendimentos = contagem_total_atendimento_doutor(medico)
    contagem_por_medico[medico] = numero_atendimentos


numero_medicos = len(medicos)
print(f"Tamanho da coluna 'médicos': {numero_medicos}")
print("Contagem de atendimentos por médico:")
for medico, contagem in contagem_por_medico.items():
    print(f"{medico}: {contagem}")

# Cria um dataframe vazio e armazena em uma variavel
df_medico_quant_atend = pd.DataFrame({'medico': medicos, 'quantidade_atendimentos': numero_atendimentos})
print(df_medico_quant_atend)
