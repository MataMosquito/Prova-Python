import pandas as pd
import matplotlib.pyplot as plt

Tiltanic = pd.read_csv('titanic.csv')
Tiltanic = Tiltanic.sort_values('Name')

print(Tiltanic['Name'])