import pandas as pd
import matplotlib.pyplot as plt

Tiltanic = pd.read_csv('titanic.csv')
Tiltanic.to_excel('titanic.xlsx')

