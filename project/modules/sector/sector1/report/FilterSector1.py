import pandas as pd

import project as md
from project.modules.util import Time

anoMaster, mesMaster = Time.dataMaster()

#! Realiza filtros necessários na base
def base_confidencial(df, path):

    decimal = eval(f'md.BaseTypeSector1.{path}_decimal()')
    for col in decimal:
        df[col] = df[col].astype(float).astype(int)

    datetime = eval(f'md.BaseTypeSector1.{path}_datetime()')
    for col in datetime:
        df[col] = df[col].astype('datetime64[ns]')

    string = eval(f'md.BaseTypeSector1.{path}_string()')
    for col in string:
        df[col] = df[col].astype('string')

    df = df[[
        'coluna_confidencial',
        ...
    ]]

    # MUDAR COLUNAS CONFLITO PARA TIPO INTEIRO
    cols = ['coluna_confidencial','coluna_confidencial','coluna_confidencial','coluna_confidencial']
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    # FILTRAR ANO ATUAL + VAZIAS E TIRAR REPROVADOS
    sagre = pd.to_datetime(df['coluna_confidencial'], dayfirst=True)
    df = df.loc[(sagre.dt.year == anoMaster) | (df['coluna_confidencial'].isnull())]
    df = df[~df['coluna_confidencial'].str.contains('filtro_confidencial', case=False)]

    return df


