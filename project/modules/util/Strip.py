
#! Remove espaços vazios
def strip(df, lista):
    for i in lista:
        df[i] = df[i].str.strip()
