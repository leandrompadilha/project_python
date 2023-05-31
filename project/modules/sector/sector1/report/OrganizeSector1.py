
#! Organiza colunas e nomes do resultado
def analitico(df, segmento, mesMaster, anoMaster):

       # INÍCIO TRATAMENTO
       df = df[['coluna_confidencial', 'coluna_confidencial', 'coluna_confidencial', 'coluna_confidencial']]

       # SAGRE EM BRANCO = dat_LibComercial
       for index, linha in df.iterrows():
              if df.dat_Sagre[index] == '':
                     df.dat_Sagre[index] = df['coluna_confidencial'][index]

       df = df.drop('dat_LibComercial', axis=1)

       # AGRUPAR E RENOMEAR NOME REGIONAIS
       df.loc[df['nom_Regional'] == 'regional_confidencial', 'nom_Regional'] = 'regional_confidencial'
       df.loc[df['nom_Regional'] == 'regional_confidencial', 'nom_Regional'] = 'regional_confidencial'
       df.loc[df['nom_Regional'] == 'regional_confidencial', 'nom_Regional'] = 'regional_confidencial'
       df.loc[df['nom_Regional'] == 'regional_confidencial', 'nom_Regional'] = 'regional_confidencial'
       df.loc[df['nom_Regional'] == 'regional_confidencial', 'nom_Regional'] = 'regional_confidencial'
       df.loc[(df['nom_Regional'] == 'regional_confidencial') & (df['regional_confidencial'] == 'regional_confidencial'),
              'nom_Regional'] = 'regional_confidencial'
       df.loc[(df['nom_Regional'] == 'regional_confidencial') & (df.SPO == 'regional_confidencial'),
              'nom_Regional'] = 'regional_confidencial'

       df.rename({'nom_Regional': 'regional'}, axis=1, inplace=True)
       df = df.drop('regional_confidencial', axis=1)

       df = df.assign(realizado=1)
       df = df.groupby('regional')['realizado'].size().reset_index()
       df.insert(0, 'segmento', segmento, allow_duplicates=False)

       df.insert(1, 'ano', anoMaster, allow_duplicates=False)
       df.insert(2, 'mes', mesMaster, allow_duplicates=False)

       return df