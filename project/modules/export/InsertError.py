import pandas as pd


#! Insere erros encontrados na base de resumo
def error(df_erro, path, file, col, sheet, sector):
    final_path = f"dist\\error_report\\{sector}\\{path}\\{file}.xlsx"


    if len(df_erro[col]) > 0:
        with pd.ExcelWriter(final_path, mode="a") as writer:
            df_erro.to_excel(writer, sheet_name=sheet, index=False)
