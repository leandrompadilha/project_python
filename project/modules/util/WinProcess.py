import os

import psutil
import pywinauto

os.system("cls")

#! Exibe lista de processos em execução no Windows
def fullList():
    processos = psutil.process_iter()

    for processo in processos:
        print(processo.name())


def searchList(string):
    for processo in psutil.process_iter():
        try:
            nome_processo = processo.name().lower()
            if string in nome_processo:
                pid = processo.pid
                handle_janela = pywinauto.findwindows.find_windows(process=pid)[0]
                nome_janela = pywinauto.controls.hwndwrapper.HwndWrapper(handle_janela).texts()[0]
                print('Nome processo:', nome_processo)
                print('Nome janela:', nome_janela + '\n')
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass




