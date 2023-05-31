import datetime as dt
import logging

now = dt.datetime.now().strftime('%d_%m_%Y-%H_%M')

#! Salva em um arquico o relatório de erro com data e horário atual
def save(path, e):
    logging.basicConfig(filename=f'dist\\error_log\\{path}-{now}h.log', level=logging.DEBUG)
    logging.exception(e)
