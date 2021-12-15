import pandas as pd
import matplotlib.pyplot as plt

Tiltanic = pd.read_csv('titanic.csv')
Tiltanic.rename(columns={'PassengerId': 'IdPassageiro'}, inplace = True)
Tiltanic.rename(columns={'Survived': 'Sobreviveu'}, inplace = True)
Tiltanic.rename(columns={'Pclass': 'Pclase'}, inplace = True)
Tiltanic.rename(columns={'Name': 'Nome'}, inplace = True)
Tiltanic.rename(columns={'Sex': 'Sexo'}, inplace = True)
Tiltanic.rename(columns={'Age': 'Idade'}, inplace = True)
Tiltanic.rename(columns={'Fare': 'Tarifa'}, inplace = True)
Tiltanic.rename(columns={'Cabin': 'Cabine'}, inplace = True)
Tiltanic.rename(columns={'Embarked': 'Embarcou'}, inplace = True)

print(Tiltanic)