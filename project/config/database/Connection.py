import os
from datetime import date
from datetime import datetime as dt
from time import sleep

import pandas as pd
import sqlalchemy
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, text)
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate

import project as md


#! Arquivo de conexão e manipulação do banco de dados
def conx(db_name):

    md.MessageColor.default('Estabelecendo conexão com o banco de dados...')
    db_pass = os.getenv('DB_PASS')
    engine = sqlalchemy.create_engine(
        f'mysql+pymysql://root:{db_pass}@localhost/{db_name}')

    try:
        connection = engine.connect()
        md.MessageColor.green('Conexão estabelecida com sucesso!')
    except:
        md.MessageColor.red(
            'Não foi possível estabelecer uma conexão com o banco de dados.')
    sleep(3)

    Session = sessionmaker(bind=engine)
    session = Session()

    # DEFINIR CURRENT PERIOD
    today = date.today()
    now = dt.now().time()

    if now < dt.strptime('12:00', '%H:%M').time():
        period = 'manhã'
    else:
        period = 'tarde'

    return connection, engine, session, today, period


#! INSERT DATAFRAME
def insertDataFrame(df, base_name, db_name):

    connection, engine, session, today, period = conx(db_name)

    try:
        # Verificar se já existe um registro com a mesma data e período
        query = text(
            f"SELECT COUNT(*) FROM {base_name} WHERE DATE(created_at) = '{today}' AND periodo_relatorio = '{period}' LIMIT 1"
        )
        result = connection.execute(query).fetchone()[0]

        if result == 0:
            # Inserir o DataFrame no banco de dados
            df.to_sql(base_name, con=engine, if_exists='append', index=False)
            session.commit()
            print(f'Dados inseridos no banco de dados com sucesso!')
        else:
            session.rollback()
            md.MessageColor.red('Operação cancelada!')
            e = f'Já existe um registro com a mesma data e período: {today} - {period}'
            print(e)
            md.ErrorLog.save(base_name, e)

    except Exception as e:
        session.rollback()
        md.ErrorLog.save(base_name, e)
        print(f'\n{45*"/"}\nOcorreu um erro durante a inserção dos dados:\n',
              str(e), '\n')
    finally:
        session.close()


#! IMPORTAR DATABASE ATUAL
def importBase(table, db_name):

    _, engine, session, today, period = conx(db_name)

    query = f"SELECT * FROM {table} WHERE DATE(created_at) = '{today}' AND periodo_relatorio = '{period}'"

    with engine.connect() as con:
        df = pd.read_sql(query, con=con)
    session.close()

    return df


#! EXECUTAR QUERY
def executeQuery(query, db_name):

    connection, _, session, _, _ = conx(db_name)

    try:
        stmt = text(query)
        result = connection.execute(stmt)
        return result
    except Exception as e:
        session.rollback()
        print(f'Ocorreu um erro ao executar a query: {str(e)}')
    finally:
        session.close()
