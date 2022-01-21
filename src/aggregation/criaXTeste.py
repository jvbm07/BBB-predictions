import pandas as pd

path = "../../data/intermin/participantes/participantes2022.csv"
novo = pd.read_csv(path)
X = novo.drop(["Posição"], axis=1)
X.to_csv("../../data/processed/participantes/teste.csv")