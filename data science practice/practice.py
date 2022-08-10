import os
import pandas as pd
import numpy as np
os. chdir('data science practice')
mixer_data = pd.read_csv('Bosch Pro 1000W.csv')
mixer_data1 = mixer_data.copy(deep=True)

print(mixer_data1.size)
print(mixer_data1.index)
print(mixer_data1.columns)
print(mixer_data1.shape)
print(mixer_data1.memory_usage())
print(mixer_data1.ndim)
print(mixer_data1.head(5))
print(mixer_data1.tail(3))
