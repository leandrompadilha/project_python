import zipfile

import pandas as pd


#! Import das bases extraídas de um arquivo zip com colunas predefinidas
def base_confidencial(path):
    with zipfile.ZipFile(path) as z:
        cols = [
        'coluna_confidencial',
        ...
        ]
        with z.open('base_confidencial.TXT') as f:
            df = pd.read_csv(f,
                             sep='|',
                             encoding='UTF-16 LE',
                             low_memory=False,
                             usecols=cols)


            df = df.rename(columns={'coluna_confidencial': 'coluna_confidencial'})

        return df

