import pandas as pd
def transformaDataIdade(niver, edicao):
    if niver[0] == '?':
        idade = "unknown"
        return idade
    ano = int(niver[6]+niver[7]+niver[8]+niver[9])
    idade = edicao-ano
    return idade
def transformaDataSigno(niver):
    ## niver é uma string dd/mm/aaaa
    if niver[0] == '?':
        signo = "unknown"
        return signo
    dia = int(niver[0]+niver[1])
    mes = int(niver[3]+niver[4])
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
        signo = "aries"
    elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
        signo = "touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        signo = "gemeos"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        signo = "cancer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        signo = "leao"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        signo = "virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        signo = "libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        signo = "escorpiao"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        signo = "sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
        signo = "capricornio"
    elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 18):
        signo = "aquario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        signo = "peixes"
    else:
        signo = "unknown"
    return signo
def transformaLocalEstado(local):
    if len(local) < 10:
        return "unknown"
    cidade, estado = map(str, local.split(', '))
    return estado
def transformaEstadoRegiao(estado):
    ## estado é uma string do tipo "estado"
    
    
    norte = ["Amazonas", "Roraima", "Rondônia", "Amapá", "Pará", "Tocantins","Acre"]
    nordeste = ["Alagoas", "Bahia", "Ceará", "Maranhão", "Piauí", "Pernambuco", "Paraíba", "Rio Grande do Norte","Sergipe"]
    sul = ["Paraná", "Rio Grande do Sul" , "Santa Catarina"]
    sudeste = ["Espírito Santo", "Minas Gerais", "Rio de Janeiro" , "São Paulo"]
    centroOeste = ["Goiás", "Mato Grosso", "Mato Grosso do Sul" , "Distrito Federal"]
    if estado in norte:
        return "Norte"
    elif estado in nordeste:
        return "Nordeste"
    elif estado in sul:
        return "Sul"
    elif estado in sudeste:
        return "Sudeste"
    elif estado in centroOeste:
        return "Centro-Oeste"
    else:
        return "unknown"
def criaTabelaParticipantes(path, edicao):
    df = pd.read_csv(path)
    df.drop(columns=['Ref.','Resultado'],inplace=True)
    df['Posição'] = range(1, len(df) + 1)
    signo = df['Data de nascimento'].apply(transformaDataSigno)
    df['Signo'] = signo
    local = df['Origem']
    estado = local.apply(transformaLocalEstado)
    df['Estado'] = estado
    regiao = estado.apply(transformaEstadoRegiao)
    df['Região'] = regiao
    idade = df.apply(lambda x: transformaDataIdade(x['Data de nascimento'], edicao), axis=1)
    df['Idade'] = idade
    print(df.head())



prefix = "../../data/external/participantes/participantes20"
for i in range(1,22):
    if i < 10:
        suffix = "0" + str(i) + ".csv"
    else:
        suffix = str(i) + ".csv"
    path = prefix + suffix
    print(i)
    edicao = 2000 + i
    criaTabelaParticipantes(path, edicao)

