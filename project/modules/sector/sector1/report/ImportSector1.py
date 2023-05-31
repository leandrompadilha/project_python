import glob
import os

import pandas as pd


#! Importa arquivos utilizados como referência para os relacionamentos das bases
def referenceCsv(path):

    csv_files = glob.glob(os.path.join(path))

    for file in csv_files:
        df = pd.read_csv(file, encoding='ANSI', sep=';', low_memory=False)

    df.dropna(inplace=True)

    return df


def copiaMaster(path):

    cols = ['coluna_confidencial', 'coluna_confidencial']

    csv_files = glob.glob(os.path.join(path))

    for files in csv_files:
        df = pd.read_csv(files,
                         encoding='ANSI',
                         sep=';',
                         low_memory=False,
                         usecols=cols)

    df.rename({
        'coluna_confidencial': 'coluna_confidencial',
        'coluna_confidencial': 'coluna_confidencial'
    },
              axis=1,
              inplace=True)

    df.dropna(inplace=True)

    return df