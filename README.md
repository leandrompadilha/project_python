# SCRIPT_RESUME - ETL

### IMPORT
- Importa as bases

### VALIDATION
- Remove linhas com ids vazios
- Remove ids duplicados
- Valida CEP
- Valida padrão armário
- Valida padrão datas
- Valida numerais
- Define colunas de acordo com seu tipo(Int, Datetime, String)
- Extrai em um arquivo Excel um resumo de erros com as linhas e colunas encontradas com divergências para possível correção

### FILTER
- Converte todas as strings para letras minúsculas e sem acento
- Cria a coluna periodo_relatorio classificado em antes do meio dia(manhã) e depois(tarde)
<br><br>

## INSERÇÃO NO BANCO DE DADOS

### INSERT BD
- Cria a coluna created_at e updated_at com a data atual
- Verifica se a tabela com a mesma data e período já existe no bd, caso sim, cancela a inserção
- Reporta qualquer erro na execução do código em um arquivo contendo o dia e horário do erro
- Insere no banco de dados base tratada
<br><br>

## EXTRAÇÃO DE RELATÓRIOS SECTOR1

### IMPORT
- Importa bases do banco de dados
- Importa base_referencia_confidencial
...
...
...
...


### FILTER
#### base_confidencial
- Filtra ano atual + vazias
- Tira reprovados

#### base_confidencial
- Quando liberado comercial, exclui linhas que a coluna_confidencial não seja o ano atual

#### Report Sector1
- Zera coluna realizado para atualização de valores
- Realiza proc com a base controle_Sector1 para garantir valores corretos conforme inserção manual na tabela

#### Todas as bases
- Nas colunas strings transforma letras em minúsculas e sem acento

### PROCS
#### base_confidencial

- Altera regional_confidencial pra regional_confidencial
- Proc com base_confidencial
...

- Filtra apenas linhas vazias da coluna base_confidencial
...


### EXTRACT VALUES
- Filtra colunas para obter os valores de B2B, B2C, CONDDM e ALIVIOS separadamente
- Gera uma nova tabela agrupando os valores em seis regionais (...)
- Insere estes valores na tabela Report Sector1

### SAVE
- Salva o arquivo Report Sector1 com os novos valores prontos para serem utilizados como atualização do dashboard do Power BI
<br><br>
