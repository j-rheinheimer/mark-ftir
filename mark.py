"""
Projeto MARK:
Análise de grau de conversão
Dados de IRFT
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import glob

files = glob.glob(
    pathname='/home/rheinheimer/Dropbox/Programas/lab_mav/mark_project/data/*'
)

for file in files:
    df = pd.read_csv(
            filepath_or_buffer=file,
            sep=';',
            header=None,
            index_col=False,
            engine='python',
        )

    df.columns = ['wave_number', 'intensity']
    wave_number = np.array(df['wave_number'])
    intensity = np.array(df['intensity'])

    degree = intensity[1633]/intensity[1695]

    print(degree)

plt.figure()
