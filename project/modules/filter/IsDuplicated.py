import project as mod

#! Encontra padrões com erro e registra no resumo
def isDuplicated(df, path, file, col, sector):

    df_error = df[df[col].duplicated(keep=False)]
    df_error = df_error.drop_duplicates(subset=col)

    mod.InsertError.error(df_error, path, file, col, "id duplicado", sector)

    mod.InsertSummary.summary(path, file, col, df_error[col].count(),
                              "REMOVIDO", "id duplicado", sector)
    df.drop_duplicates(subset=col, inplace=True)

    return df
