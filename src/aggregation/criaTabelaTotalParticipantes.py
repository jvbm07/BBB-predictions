import pandas as pd
df = pd.read_csv("../../data/intermin/participantes/participantes2001.csv")
for i in range(2002,2022):
    aux = pd.read_csv("../../data/intermin/participantes/participantes" + str(i) + ".csv" )
    df = df.append(aux)
df.to_csv("../../data/processed/participantes/participantesTotais.csv")