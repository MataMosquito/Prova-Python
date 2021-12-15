import pandas as pd
import matplotlib.pyplot as plt

Tiltanic = pd.read_csv('titanic.csv')

Tiltanic['Sex']=Tiltanic['Sex'].replace(['male'],"masculino")
Tiltanic['Sex']=Tiltanic['Sex'].replace(['female'],"FEMININO")

print(Tiltanic)