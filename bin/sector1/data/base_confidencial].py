import os
import sys
import traceback
from time import sleep

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir,
                     os.path.pardir)))
import project as md

md.Warnings.none()

base_name = 'base_confidencial'
file = 'REPORT - base_confidencial'
path = md.PathSector1.path()
sector = 'sector1'

#! Arquivo principal de execução dos script
#! Realiza 3 tentativas em caso de erro inesperado, acima disso é gerado um relatório com o erro encontrado
def main():
    num_attempts = 0
    max_attempts = 3

    while True:
        try:

            def run_code():
                md.Start.code('project', 'BASE CONFIDENCIAL', base_name)
                md.CreateResume.create(base_name, file, sector)
                md.MessageColor.default('Import...')
                df = md.ImportBase.base_confidencial(path[base_name])
                md.MessageColor.default('Validation...')
                df = md.ValidationSector1.validation(df, base_name, file,sector)
                md.MessageColor.default('Filter...')
                df = md.BaseFilter.filter(df, base_name, sector)
                md.MessageColor.default('Insert Database...')
                md.Connection.insertDataFrame(df, base_name, sector)

            md.Run.code(run_code, 'project', '', base_name)
            break

        except PermissionError as e:
            num_attempts += 1
            if num_attempts >= max_attempts:
                md.MessageColor.default(
                    'Número máximo de tentativas alcançado. Saindo do programa.'
                )
                md.ErrorLog.save(base_name, e)
                break
            else:
                md.MessageColor.default(
                    'Erro de permissão. Tentando novamente...')
                sleep(3)

        except Exception as e:
            traceback.print_exc()
            md.ErrorLog.save(base_name, e)
            break


if __name__ == '__main__':
    main()


