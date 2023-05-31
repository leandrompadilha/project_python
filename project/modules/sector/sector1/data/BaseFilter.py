from datetime import datetime as dt

import project as md


#! Realiza tratamento padrão nas bases e cria uma nova coluna para filtro de período de extração
def filter(df, base, sector):

    # CONVERSÃO DE STRINGS
    sector = sector.capitalize()
    strings = eval(f"md.BaseType{sector}.{base}_string()")
    md.Strip.strip(df, strings)
    for string in strings:
        df[string].fillna("", inplace=True)
        md.RemoveAccents.tiny(df, string)
        df[string] = df[string].str.encode('utf-8', 'ignore').replace('"', '', regex=True).replace(';','',regex=True) # CONVERTER STRINS EM UTF-8 E REPLACE

    # CRIA NOVA COLUNA COM O PERÍODO DA EXTRAÇÃO DA BASE
    now = dt.now().time()
    if now < dt.strptime('12:00', '%H:%M').time():
        period = 'manhã'
    else:
        period = 'tarde'

    df['periodo_relatorio'] = period

    return df
