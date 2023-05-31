import re

import numpy as np

import project as md

regexCep = re.compile(r"(\d{7,8})")

#! Encontra padrões com erro e registra no resumo
def isCep(df, path, file, col, sector):

    df[col] = df[col].astype("string")
    df.loc[df[col].isnull(), col] = "vazio"
    df_error = df.loc[~df[col].str.contains(regexCep)]
    md.InsertError.error(df_error, path, file, col, f"{col} erro", sector)

    md.InsertSummary.summary(
        path, file, col, df_error[col].count(), "NÃO REMOVIDO", f"{col} erro", sector
    )

    df.loc[~df['coluna_confidencial'].str.contains(regexCep), "coluna_confidencial"] = np.nan
    df["coluna_confidencial"] = df["coluna_confidencial"].astype(float)

    return df
