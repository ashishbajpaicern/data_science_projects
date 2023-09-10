import os
import pandas as pd
import numpy as np

apy_data = pd.read_csv('apy_2.csv', na_values=['??', '????'], index_col=0)
apy = apy_data.copy()

print(apy['Season'].value_counts())
