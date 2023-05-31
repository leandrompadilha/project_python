import pandas as pd

import project as md


#! Cria um arquivo de resumo que serve como base para inserção dos valores encontrados com erro nas bases tratadas
def create(base_name, file, sector):

    # CRIANDO ARQUIVO REPORT
    md.MessageColor.default(f'Tratando base "{base_name}"...')
    md.DeleteFileIfExists.deleteExcel(base_name, file, sector)
    resumo = pd.DataFrame(columns=["Coluna", "Qtd Linhas", "Ação", "Motivo"])
    md.ExportBases.salvarExcelResumo(resumo,base_name,file,"RESUMO", sector)
