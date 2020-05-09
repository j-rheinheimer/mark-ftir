"""
MARK project:
Degree conversion analysis
FTIR data
"""

import matplotlib.pyplot as plt
import pandas as pd
import glob

wsl_path = '/mnt/c/Users/jprhe/Dropbox/Codes/Projects/mark/data/*'
linux_path = '/home/rheinheimer/Dropbox/Codes/Projects/mark/data/*'
windows_path = 'C:/Users/jprhe/Dropbox/Codes/Projects/mark/Data/*'


def conversion_degreee(n1, n2, path, time_step, separator, header):
    """
    Function that makes the calculus and plot the graphic of the
    conversion degree of polymerization about FTIR data.

    Parameters:

    n1 (int): Value of the first peak

    n2 (int): Value of the second peak

    path (string): Path to the directory with the data.
    Example: '/home/rheinheimer/Dropbox/Codes/Python/lab-mav/mark/data/*'
    Observation: The '*' is mandatory

    time_step (int/float): Time step of the measures
    Examples: 1, 0.2, 3.5

    separator (string): The separator between the data columns
    Examples: ';' ',' '  '

    header (string): Header of the file. If none please insert 'None'
    """
    files = glob.glob(
        pathname=path
    )

    degree_vector = []
    time_vector = []

    cont = 0
    for file in sorted(files):
        cont = cont + time_step
        df = pd.read_csv(
            filepath_or_buffer=file,
            sep=separator,
            header=header,
            index_col=False,
            engine='python',
        )

        df.columns = ['wave_number', 'intensity']
        degree = df.intensity[n1]/df.intensity[n2]
        degree_vector.append(degree)
        time_vector.append(cont)

    with open('degree_output.txt', 'w') as degree_output:
        degree_output.writelines(str(degree_vector))

    with open('time_step_output.txt', 'w') as time_step_output:
        time_step_output.writelines(str(time_vector))

    plt.figure()
    plt.xlabel('Time')
    plt.ylabel('Conversion degree')
    plt.plot(time_vector, degree_vector)
    plt.show()
