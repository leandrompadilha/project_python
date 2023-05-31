import glob
import os
from datetime import datetime as dt

import pandas as pd


#! Extrai variáveis contendo informações de tempo
def time(segundos):
    minutos, segundos = divmod(segundos, 60)
    segundos, milissegundos = divmod(segundos * 1000, 1000)
    return minutos, segundos, milissegundos


def anoAtual():
    anoAtual = dt.today().year
    return anoAtual


def dataMaster():
    path = os.path.join('project', 'src', 'nome_confidencial', f'nome_confidencial {dt.today().month} {dt.today().year}.csv')
    csv_files = glob.glob(path)

    for file in csv_files:
        file_name = os.path.basename(file)
        anoMaster = file_name[17:21]
        anoMaster = pd.to_numeric(anoMaster)
        mesMaster = file_name[13:16].lower()

    return anoMaster, mesMaster

dataMaster()
