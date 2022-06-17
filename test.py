import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

print("Hello World!")

df = pd.read_csv('lingerie.csv')

df.drop(df.filter(regex="Unnamed"), axis=1, inplace=True)

print(df['price'])
