import re

import project as md

#! Encontra padrões com erro e registra no resumo
def isDecimal(df, base_name, file, col, sector):

    regex = re.compile(r'^\d+(\.\d+)?$')

    df[col] = df[col].astype('string')
    df.loc[df[col].isnull(), col] = '0'

    df_error = df.loc[~df[col].str.contains(regex)]
    md.InsertError.error(df_error, base_name, file, col, f'{col} erro', sector)
    md.InsertSummary.summary(base_name, file, col, df_error[col].count(), 'NÃO REMOVIDO',
                             f'{col} erro', sector)

    df.loc[~df[col].str.contains(regex), col] = '00'

    return df
