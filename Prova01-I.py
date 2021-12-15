import pandas as pd
import matplotlib.pyplot as plt

Tiltanic = pd.read_csv('titanic.csv')

TiltanicSurv = Tiltanic.groupby(['Pclass'])['Survived'].count()

TiltanicSurv.plot(kind = 'bar')

plt.title("Sobreviventes por Classe")
plt.ylabel('Sobreviventes')
plt.xlabel('Classes')


plt.show()