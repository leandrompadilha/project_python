import re

import project as mod

regexArmarioCorreto = re.compile(
    r"(\d{5}[a-zA-Z]{2}$|[a-zA-Z]\d[a-zA-Z]\d{2}$|[a-zA-Z]\d{2}$)"
)
regexArmarioGeral = re.compile(
    r"(\d{5}[a-zA-Z]{2}$|[a-zA-Z]\d[a-zA-Z]\d{2}$|[a-zA-Z]\d[a-zA-Z]\d{2}$|\w{1,50})"
)

#! Encontra padrões com erro e registra no resumo
def isCabinet(df, path, file, col, pathCabinet, sector):

    df[col] = df[col].astype("string")
    df.loc[df[col].isnull(), col] = "vazio"
    df.loc[df[col] == "-", col] = "vazio"

    df_error = df.loc[~df[col].str.contains(regexArmarioCorreto)]

    mod.DeleteFileIfExists.deleteCSV(path, pathCabinet, sector)
    mod.ExportBases.salvarCsvErro(df_error, path, pathCabinet, 'coluna_confidencial', sector)

    mod.InsertSummary.summary(
        path, file, col, df_error[col].count(), "NÃO REMOVIDO (arquivo externo)", f"{col} erro", sector
    )

    return df
