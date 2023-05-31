projeto_modelo
 ┣ .vscode
 ┃ ┗ settings.json
 ┣ bin
 ┃ ┣ sector1
 ┃ ┃ ┣ data
 ┃ ┃ ┃ ┗ base_confidencial].py
 ┃ ┃ ┗ report
 ┃ ┃ ┃ ┗ report_sector1.py
 ┃ ┗ run_routine.bat
 ┣ dist
 ┃ ┣ error_log
 ┃ ┣ error_report
 ┃ ┃ ┗ sector1
 ┃ ┃ ┃ ┗ arquivo com resumo de erros
 ┃ ┗ report
 ┃ ┃ ┗ report_sector1
 ┃ ┃ ┃ ┗ arquivo com report final
 ┣ project
 ┃ ┣ config
 ┃ ┃ ┣ database
 ┃ ┃ ┃ ┃ ┣ Connection.cpython-310.pyc
 ┃ ┃ ┃ ┃ ┣ Connection.cpython-311.pyc
 ┃ ┃ ┃ ┃ ┗ Connection.cpython-39.pyc
 ┃ ┃ ┃ ┗ Connection.py
 ┃ ┃ ┣ run_time
 ┃ ┃ ┃ ┗ sector1.json
 ┃ ┃ ┗ sql
 ┃ ┃ ┃ ┗ Sector1.sql
 ┃ ┣ modules
 ┃ ┃ ┣ export
 ┃ ┃ ┃ ┣ InsertError.py
 ┃ ┃ ┃ ┗ InsertSummary.py
 ┃ ┃ ┣ filter
 ┃ ┃ ┃ ┣ IsCabinet.py
 ┃ ┃ ┃ ┣ IsCep.py
 ┃ ┃ ┃ ┣ IsDate.py
 ┃ ┃ ┃ ┣ IsDecimal.py
 ┃ ┃ ┃ ┣ IsDuplicated.py
 ┃ ┃ ┃ ┗ IsNull.py
 ┃ ┃ ┣ sector
 ┃ ┃ ┃ ┗ sector1
 ┃ ┃ ┃ ┃ ┣ data
 ┃ ┃ ┃ ┃ ┃ ┣ BaseFilter.py
 ┃ ┃ ┃ ┃ ┃ ┣ BaseTypeSector1.py
 ┃ ┃ ┃ ┃ ┃ ┣ CreateResume.py
 ┃ ┃ ┃ ┃ ┃ ┣ DeleteFileIfExists.py
 ┃ ┃ ┃ ┃ ┃ ┣ ImportBase.py
 ┃ ┃ ┃ ┃ ┃ ┗ ValidationSector1.py
 ┃ ┃ ┃ ┃ ┣ report
 ┃ ┃ ┃ ┃ ┃ ┣ AccSector1.py
 ┃ ┃ ┃ ┃ ┃ ┣ ExtractSector1.py
 ┃ ┃ ┃ ┃ ┃ ┣ FilterSector1.py
 ┃ ┃ ┃ ┃ ┃ ┣ ImportSector1.py
 ┃ ┃ ┃ ┃ ┃ ┣ InsertSector1.py
 ┃ ┃ ┃ ┃ ┃ ┣ OrganizeSector1.py
 ┃ ┃ ┃ ┃ ┃ ┗ ProcSector1.py
 ┃ ┃ ┃ ┃ ┗ PathSector1.py
 ┃ ┃ ┗ util
 ┃ ┃ ┃ ┣ Close.py
 ┃ ┃ ┃ ┣ ErrorLog.py
 ┃ ┃ ┃ ┣ ExportBases.py
 ┃ ┃ ┃ ┣ Json.py
 ┃ ┃ ┃ ┣ MessageColor.py
 ┃ ┃ ┃ ┣ RemoveAccents.py
 ┃ ┃ ┃ ┣ Run.py
 ┃ ┃ ┃ ┣ SendSmtp.py
 ┃ ┃ ┃ ┣ Start.py
 ┃ ┃ ┃ ┣ Strip.py
 ┃ ┃ ┃ ┣ Time.py
 ┃ ┃ ┃ ┣ Warnings.py
 ┃ ┃ ┃ ┗ WinProcess.py
 ┃ ┣ src
 ┃ ┃ ┣ databases here
 ┃ ┃ ┗ reference files here
 ┃ ┗ __init__.py
 ┣ test
 ┃ ┗ test.py
 ┗ script.md