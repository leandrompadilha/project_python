meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun',
         'jul', 'ago', 'set', 'out', 'nov', 'dez']

#! Realizado cálculo de valores acumulados dos meses anteriores
def accumulated(df, segmento, regional, mesMaster, anoMaster):

    cum = 0
    for mes in meses:
       df.loc[
              (df['coluna_confidencial'] == segmento)
              & (df['ano'] == anoMaster)
              & (df['mes'] == mes)
              & (df['regional'] == regional)
              & (df['realizado'] != 0)
              & (df['mes'] != mesMaster),
              'ac realizado'] = df['realizado'] + cum

       cum += df.loc[
              (df['segmento'] == segmento)
              & (df['ano'] == anoMaster)
              & (df['mes'] == mes)
              & (df['regional'] == regional)]['realizado']


       # REFAZER MÊS ATUAL
       df.loc[
              (df['segmento'] == segmento)
              & (df['ano'] == anoMaster)
              & (df['mes'] == mesMaster)
              & (df['regional'] == regional),
              'ac realizado'] = cum

       # COPY AC PREVISTO
       ac_previsto = df.loc[
              (df['segmento'] == segmento)
              & (df['ano'] == anoMaster)
              & (df['mes'] == mesMaster)
              & (df['regional'] == regional),
              'ac previsto']

       df.loc[
              (df['segmento'] == segmento)
              & (df['ano'] == anoMaster)
              & (df['mes'] == mesMaster)
              & (df['regional'] == regional),
              'ac previsto atual'] = ac_previsto

       # COPY AC REALIZADO
       ac_realizado = df.loc[
              (df['segmento'] == segmento)
              & (df['ano'] == anoMaster)
              & (df['mes'] == mesMaster)
              & (df['regional'] == regional),
              'ac realizado']

       df.loc[
              (df['segmento'] == segmento)
              & (df['ano'] == anoMaster)
              & (df['mes'] == mesMaster)
              & (df['regional'] == regional),
              'ac realizado atual'] = ac_realizado