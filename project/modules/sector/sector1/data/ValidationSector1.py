import project as md


#! Executa as validações
def validation(df, base_name, file, sector):

    # VALIDAÇÕES
    df = md.IsNull.isNull(df, base_name, file, 'coluna_confidencial', sector)
    df = md.IsDuplicated.isDuplicated(df, base_name, file, 'coluna_confidencial', sector)
    df = md.IsCep.isCep(df, base_name, file, 'coluna_confidencial', sector)
    df = md.IsCabinet.isCabinet(df, base_name, file, 'coluna_confidencial',
                                f'coluna_confidencial ({base_name})', sector)

    decimal = eval(f'md.BaseTypeSector1.{base_name}_decimal()')
    for col in decimal:
        df = md.IsDecimal.isDecimal(df, base_name, file, col, sector)
        df[col] = df[col].astype(float).astype(int)

    datetime = eval(f'md.BaseTypeSector1.{base_name}_datetime()')
    for col in datetime:
        df = md.IsDate.isDate(df, col, base_name, file, sector)
        df[col] = df[col].astype('datetime64[ns]')

    string = eval(f'md.BaseTypeSector1.{base_name}_string()')
    for col in string:
        df[col] = df[col].astype('string')

    return df
