import os
import pathlib

#! Delete arquivo de resumo caso existam para refazê-los de modo mais atualizado
def deleteCSV(path, file, sector):
    file = pathlib.Path(f'dist\\error_report\\{sector}\\{path}\\{file}.csv')
    if file.exists():
        os.remove(file)


def deleteExcel(path, file, sector):
    file1 = pathlib.Path(f'dist\\error_report\\{sector}\\{path}\\{file}.xlsx')
    if file1.exists():
        os.remove(file1)

    file2 = pathlib.Path(
        f'dist\\error_report\\{path}\\{sector}\\coluna_confidencial ({path}).csv')
    if file2.exists():
        os.remove(file2)
