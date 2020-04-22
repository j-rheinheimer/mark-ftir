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
    pathname='/home/rheinheimer/Dropbox/Codes/Python/lab-mav/mark/data/*'
)

n1 = 1633
n2 = 1695

degree_vector = []
time_vector = []

cont = 0
for file in sorted(files):
    cont = cont + 1
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
    degree = intensity[n1]/intensity[n2]
    degree_vector.append(degree)
    time_vector.append(cont)

plt.figure()
plt.xlabel('Time')
plt.ylabel('Conversion degree')
plt.plot(time_vector, degree_vector)
plt.show()

with open('degree_output.txt', 'w') as degree_output:
    degree_output.writelines(str(degree_vector))

with open('time_step_output.txt', 'w') as time_step_output:
    time_step_output.writelines(str(time_vector))
