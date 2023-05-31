import datetime as dt
import os

import project as md


#! Apresenta mensagem personalizada de início de execução do script
def code(project, name, path):

    os.system("cls")

    try:
        time = md.Json.read(f'{project}\\config\\run_time\\{path}.json')
        now, preview = md.Run.time_execution(time)
        md.MessageColor.start_1(name, now, preview)

    except FileNotFoundError:
        now = dt.datetime.now().strftime("%H:%M:%S")
        md.MessageColor.start_0(name, now)
