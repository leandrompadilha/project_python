import re
from datetime import datetime as dt

import numpy as np
import pandas as pd

import project as md


#! Encontra padrões com erro e registra no resumo
def isDate(df, col, base_name, file, sector):
    df[col] = df[col].astype('string')
    df[col] = df[col].str.slice(start=0, stop=10)
    df[col] = df[col].replace('-',
                              '/').str.replace(r'^(\d{4})/(\d{2})/(\d{2})$',
                                               r'\3/\2/\1',
                                               regex=True)

    regex_date = re.compile(r'\d{2}/\d{2}/\d{4}')
    mask = df[col].str.match(regex_date)
    df.loc[~mask, col] = np.nan

    # Filtra apenas anos dentro do range
    anos = range(1990, anoAtualMais())
    anos_str = [str(ano) for ano in anos]
    anos_range = '|'.join(anos_str)

    df_error = df.loc[~df[col].str.contains(anos_range)]
    md.InsertError.error(df_error, base_name, file, col, f'{col} erro', sector)
    md.InsertSummary.summary(base_name, file, col, df_error[col].count(), 'NÃO REMOVIDO',
                             f'{col} erro', sector)


    df.loc[~df[col].str.contains(anos_range), col] = np.nan
    df[col] = pd.to_datetime(df[col], format='%d/%m/%Y')


    return df


def anoAtualMais():
    anoAtual = dt.today().year
    return anoAtual + 4