import pandas as pd
import matplotlib.pyplot as plt

Tiltanic = pd.read_csv('titanic.csv')

Tiltanic.drop('SibSp', inplace=True, axis=1)
Tiltanic.drop('Parch', inplace=True, axis=1)
Tiltanic.drop('Ticket', inplace=True, axis=1)

print(Tiltanic)