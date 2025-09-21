#Part 1 – Pandas DataFrames
#1.Set your working directory and import the dataset Enaho01A-2023-300.csv using Pandas.
import pandas as pd
import os

os.chdir("D:\OneDrive - Superintendencia Nacional de Servicios de Saneamiento\TRABAJO REMOTOV1\Escritorio\Diplomado_PUCP\MODULO 300\906-Modulo03")  
df = pd.read_csv("Enaho01A-2023-300.csv", encoding="latin1")

#Read and display the first 5 rows.
print("Primeras 5 filas:")
print(df.head())

#Convert the column names into a list and print it.
col_names = df.columns.tolist()
print("\nNombres de columnas:")
print(col_names)

#Check the data types of the DataFrame.
print("\nTipos de datos:")
print(df.dtypes)

#Select a subsample containing the variables ['CONGLOME', 'VIVIENDA', 'HOGAR', 'CODPERSO'] and between 3–5 additional variables of your interest.
vars_base = ['CONGLOME', 'VIVIENDA', 'HOGAR', 'CODPERSO']
vars_extra = ['P101A', 'P103', 'P301A', 'P301B']  # ajusta según tu interés
df_sub = df[vars_base + vars_extra]

print("\nSubmuestra seleccionada:")
print(df_sub.head())

#2. Data Manipulation (Data Cleaning):
#Explore the DataFrame using summary functions.
print("Forma (filas, columnas):", df.shape)
print("\nInfo del DataFrame:")
print(df.info())  # tipos y no-nulos por columna

print("\nResumen numérico:")
print(df.describe(datetime_is_numeric=True))  # estadísticos de numéricas

print("\nResumen general (incluye categóricas):")
print(df.describe(include='all', datetime_is_numeric=True))