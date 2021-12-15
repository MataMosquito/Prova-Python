import pandas as pd
import matplotlib.pyplot as plt

Tiltanic = pd.read_csv('titanic.csv')

Tiltanic['Sobreviveu']=Tiltanic['Survived']

Tiltanic['Sobreviveu']=Tiltanic['Sobreviveu'].replace([0],"Nao")
Tiltanic['Sobreviveu']=Tiltanic['Sobreviveu'].replace([1],"Sim")

print(Tiltanic)