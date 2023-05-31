import pandas as pd

import project as md


#! Realiza o relacionamento das bases para obter novas colunas com valores buscados
def base_confidencial(df, spo, atc, masterPruma):

    df.loc[df['nom_Regional'] == 'regional_confidencial', 'nom_Regional'] = 'regional_confidencial'
    df = pd.merge(df, spo, on='nom_Municipio', how='left')
    df = pd.merge(df, atc, on='nom_Municipio', how='left')
    df = pd.merge(df, masterPruma, on='regional_confidencial', how='left')
    df.loc[df['nom_Regional'] == 'regional_confidencial', 'nom_Regional'] = 'regional_confidencial'
    df.loc[(df['nom_Regional'] == 'regional_confidencial') & (df['SPO'].isnull()), 'SPO'] = 'SPI'

    df = df[df['MASTER'].isnull()]
    df = df[df['ATC'].isnull()]

    return (df)



