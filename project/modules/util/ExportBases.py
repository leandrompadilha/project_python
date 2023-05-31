import os
from pathlib import Path

p = Path(os.getcwd())


#! Exporta bases e diferentes formatos
def salvarCsv(df, path):
    df.to_csv(path, index=False, sep=";", encoding="ANSI")


def salvarCsvErro(df, path, file, col, sector):
    path = f"dist\\error_report\\{sector}\\{path}\\{file}.csv"
    if len(df[col]) > 0:
        df.to_csv(path, index=False, sep=";", encoding="ANSI")


def salvarExcelResumo(df, path, file, sheet, sector):
    path = f".\\dist\\error_report\\{sector}\\{path}\\{file}.xlsx"
    df.to_excel(path, index=False, sheet_name=sheet)


def salvarCsvTeste(df, nome):
    path = f"test\\{nome}.csv"
    df.to_csv(path, index=False, sep=";", encoding="ANSI")
