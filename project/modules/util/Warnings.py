import os
import warnings

import pandas as pd


#! Desabilita informações de erro desnecessários durante a execução do script
def none():
    warnings.simplefilter(action="ignore", category=UserWarning)
    pd.set_option("chained_assignment", None)
    os.system("cls")