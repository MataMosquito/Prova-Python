import pandas as pd
import matplotlib.pyplot as plt

Tiltanic = pd.read_csv('titanic.csv')
Tiltanic.drop(Tiltanic.loc[Tiltanic['Survived'] == 0].index, inplace=True)

TiltanicSurv = Tiltanic.groupby(['Survived','Pclass'], as_index=False)['Survived'].count()

print(TiltanicSurv)
