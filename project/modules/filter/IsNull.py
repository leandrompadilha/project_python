import project as mod


def isNull(df, path, file, col, sector):

    #! Encontra padrões com erro e registra no resumo
    df_error = df[df[col].isnull()]
    df_error.insert(0, "index", df_error.index + 2, allow_duplicates=False)
    mod.InsertError.error(df_error, path, file, col, "id vazio", sector)

    mod.InsertSummary.summary(path, file, col, df_error["index"].count(),
                              "REMOVIDO", "id vazio", sector)

    df.dropna(subset=[col], inplace=True)
    df[col] = df[col].astype("int64")

    return df
