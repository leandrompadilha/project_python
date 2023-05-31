import datetime as dt
import os

import project as md


#! Mensagens personalizadas para a execução do script
# TABELA ANSI
def start_0(projeto, now):
    os.system('cls')

    print(f'\n\033[1;45m  NOME_EMPRESA  \033[0;0m\033[1;35m {projeto}\033[0;0m')
    white(f'\nInício da execução:    \033[1;41m{now}\033[0;0m')
    green('\nINICIANDO PROGRAMA')
    line()


def start_1(projeto, now, preview):
    os.system('cls')
    print(f'\n\033[1;45m  NOME_EMPRESA  \033[0;0m\033[1;35m {projeto}\033[0;0m')

    default(f'\nInício da execução:    \033[1;41m{now}\033[0;0m')
    default(f'Previsão de conclusão: \033[1;41m{preview}\033[0;0m')

    green('\nINICIANDO PROGRAMA')
    line()


def end(time):
    line()
    green('PROCESSO CONCLUÍDO')
    now = dt.datetime.now().strftime("%H:%M:%S")
    default(f'\nFim da execução:       \033[1;42m{now}\033[0;0m')

    min, sec, mili = md.Time.time(time)
    default(
        f'Tempo de execução:     \033[1;32m{min:.0f} min {sec:.0f} seg {mili:.0f} mili\033[0;0m\n'
    )



def shape(var):
    print(
        f'\033[1;33m↑ Arquivo com {var.shape[0]} linhas e {var.shape[1]} colunas\033[0;0m'
    )


def line():
    print('----------------------------------------------------------------')


# STYLES
def bold(txt):
    print(f'\033[;1m{txt}\033[0;0m\n')


def inverse(txt):
    print(f'\033[;7m{txt}\033[0;0m\n')


# COLORS
def black(txt):
    print(f'\033[1;30m{txt}\033[0;0m')


def red(txt):
    print(f'\033[1;31m{txt}\033[0;0m')


def green(txt):
    print(f'\033[1;32m{txt}\033[0;0m')


def yellow(txt):
    print(f'\033[1;33m{txt}\033[0;0m')


def purple(txt):
    print(f'\033[1;34m{txt}\033[0;0m')


def magenta(txt):
    print(f'\033[1;35m{txt}\033[0;0m')


def cyan(txt):
    print(f'\033[1;36m{txt}\033[0;0m')


def grey(txt):
    print(f'\033[1;37m{txt}\033[0;0m')


def white(txt):
    print(f'\033[1;97m{txt}\033[0;0m')

def default(txt):
    print(txt)


# BACKGROUND
def fblack(txt):
    print(f'\033[1;40m{txt}\033[0;0m')


def fred(txt):
    print(f'\033[1;41m{txt}\033[0;0m')


def fgreen(txt):
    print(f'\033[1;42m\033[1;30m{txt}\033[0;0m')


def fyellow(txt):
    print(f'\033[1;43m\033[1;30m{txt}\033[0;0m')


def fpurple(txt):
    print(f'\033[1;44m{txt}\033[0;0n')


def fmagenta(txt):
    print(f'\033[1;45m{txt}\033[0;0m')


def fcyan(txt):
    print(f'\033[1;46m{txt}\033[0;0m')


def fwhite(txt):
    print(f'\033[1;100m{txt}\033[0;0m')
