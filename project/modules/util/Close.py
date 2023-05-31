import subprocess


#! Encerra um processo do Windows
def process(window_title):

    command = f'TASKKILL /F /FI \"WINDOWTITLE eq {window_title}\" /T'

    subprocess.call(command, shell=True)