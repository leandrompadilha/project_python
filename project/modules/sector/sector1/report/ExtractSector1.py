import pandas as pd

import project as md


#! Filtros pruma para obter B2C - Mesma função para outros segmentos
def b2c(df, report_sector1, mesMaster, anoMaster):

    df = df[df['coluna_confidencial'].isin([
        'coluna_confidencial',
        ...
    ])]
    df = df[df['coluna_confidencial'].isin([
        'coluna_confidencial',
        ...
    ])]
    df = df[df['nom_SegPredio'].isin([
        'coluna_confidencial',
        ...
    ])]
    df = df[df['coluna_confidencial'].isin(['coluna_confidencial', 'coluna_confidencial'])]

    df = md.OrganizeSector1.analitico(df, 'B2C', mesMaster, anoMaster)
    report_sector1 = md.InsertSector1.analitico(df, report_sector1, 'B2C', mesMaster, anoMaster)

    return report_sector1


#! Adicionar coluna previsto no dataframe
def previsto(report_sector1, previsto):

    report_sector1 = pd.merge(report_sector1,
                     previsto,
                     on=['segmento', 'ano', 'mes ref', 'mes', 'regional'],
                     how='left')

    report_sector1 = report_sector1.drop('previsto_x', axis=1)
    report_sector1.rename({'previsto_y': 'previsto'}, axis=1, inplace=True)

    report_sector1 = report_sector1[[
        'coluna_confidencial',
        ...
    ]]

    return report_sector1
