import pandas as pd

import project as md


#! Inserir resultados na base principal
def analitico(df, report_sector1, segmento, mesMaster, anoMaster):

    # INSERIR DADOS DO MÊS TABELA report_sector1
    report_sector1 = pd.merge(report_sector1,
                     df,
                     on=['segmento', 'ano', 'mes', 'regional'],
                     how='left')

    report_sector1.loc[(report_sector1.segmento == segmento) & (report_sector1.ano == anoMaster) &
              (report_sector1.mes == mesMaster),
              'realizado_x'] = report_sector1.realizado_x + report_sector1.realizado_y

    report_sector1 = report_sector1.drop('realizado_y', axis=1)
    report_sector1.rename({'realizado_x': 'realizado'}, axis=1, inplace=True)

    # ACUMULADOS
    report_sector1.fillna(0, inplace=True)

    # AC REALIZADO
    lista = ['regional_confidencial', 'regional_confidencial', 'regional_confidencial', 'regional_confidencial', 'regional_confidencial', 'regional_confidencial']
    for i in lista:
        md.AccSector1.accumulated(report_sector1, segmento, i, mesMaster, anoMaster)

    return report_sector1