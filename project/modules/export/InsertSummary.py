import pandas as pd

#! Insere resumo de erros encontrados na base de resumo
def summary(path, file, col, qtd, acao, motivo, sector):

    final_path = f"dist\\error_report\\{sector}\\{path}\\{file}.xlsx"
    df = pd.read_excel(final_path, sheet_name="RESUMO")


    if qtd > 0:
        df.loc[len(df)] = [col, qtd, acao, motivo]

        with pd.ExcelWriter(final_path, mode="a", if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheet_name="RESUMO", index=False)




