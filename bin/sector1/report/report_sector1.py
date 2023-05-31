import os
import sys
import traceback
from time import sleep

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir)))
import project as md

md.Warnings.none()

base_name = 'report'
path = md.PathSector1.path()
sector = 'sector1'
anoMaster, mesMaster = md.Time.dataMaster()

#! Arquivo principal de execução dos script
#! Realiza 3 tentativas em caso de erro inesperado, acima disso é gerado um relatório com o erro encontrado
def main():
    num_attempts = 0
    max_attempts = 3

    while True:
        try:
            def run_code():
                md.Start.code('project', 'REPORT sector1', base_name)

                #! IMPORTS

                md.MessageColor.default('Import bases...')
                df = md.Connection.importBase('base_confidencial')

                base_referencia = md.ImportSector1.referenceCsv(path['base_confidencial'])
                ...
                ...
                ...

                #! FILTER
                md.MessageColor.default('Filter bases...')
                df = md.FilterSector1.base_confidencial(df, 'base_confidencial')

                bases = [base_referencia,base_referencia]
                bases = [md.RemoveAccents.tinyNoAccents(base) for base in bases]

                bases = [base_referencia,base_referencia,base_referencia]
                bases = [md.RemoveAccents.tinyNoAccentsCols(base) for base in bases]
                report_sector1 = md.FilterSector1.base_confidencial(report_sector1, base_referencia)

                #! PROCS
                md.MessageColor.default('Proc bases...')
                df = md.ProcSector1.base_confidencial(base_referencia, base_referencia, base_referencia, base_referencia)
                ...
                ...


                #! EXTRACT sector1 REPORT
                report_sector1 = md.ExtractSector1.b2c(df, report_sector1, mesMaster, anoMaster)
                ...
                ...

                #! SAVE
                md.ExportBases.salvarCsv(report_sector1, 'dist\\report\\report_sector1\\REPORT sector1.csv')

            md.Run.code(run_code, 'project', '', base_name)
            break

        except PermissionError as e:
            num_attempts += 1
            if num_attempts >= max_attempts:
                md.MessageColor.default('Número máximo de tentativas alcançado. Saindo do programa.')
                md.ErrorLog.save(base_name, e)
                break
            else:
                md.MessageColor.default('Erro de permissão. Tentando novamente...')
                sleep(3)

        except Exception as e:
            traceback.print_exc()
            md.ErrorLog.save(base_name, e)
            break


if __name__ == '__main__':
    main()
