import datetime as dt
import os
import timeit

import project as md


#! Função padrão para iniciar e apresentar dados referentes a execução do script
def code(run_code, project, open, path):
    time = timeit.timeit(run_code, number=1)
    md.Json.create(f'{project}\\config\\run_time\\{path}.json', time)
    md.MessageColor.end(time)
    # os.startfile(open)

def time_execution(add):
    agora = dt.datetime.now()
    nova_hora = agora + dt.timedelta(seconds=add)
    nova_hora = nova_hora.strftime("%H:%M:%S")
    agora = agora.strftime("%H:%M:%S")
    return agora, nova_hora

