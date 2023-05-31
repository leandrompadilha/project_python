import unicodedata


#! Funções para remover acentos e deixar letras minúsculas
def noAccents(txt):
    txt = str(txt)
    txt = unicodedata.normalize('NFKD', txt).encode('ASCII', 'ignore').decode('utf-8')
    return txt

def tiny(df, col):
    df[col] = df[col].apply(noAccents).str.lower().replace('.', '').replace('–', '-')


def tinyNoAccents(df):
    cols = ['coluna_confidencial']
    for col in cols:
        df[col].fillna('', inplace=True)
        tiny(df, col)
    return df


def tinyNoAccentsCols(df):
    cols = ['coluna_confidencial','coluna_confidencial','coluna_confidencial']
    for col in cols:
        df[col].fillna('', inplace=True)
        tiny(df, col)
    return df