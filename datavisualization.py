import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import numpy as np


def visualizedata(equation):
    # setting graph parameters
    plt.rcParams["figure.figsize"] = [15.00, 7]
    plt.rcParams["figure.autolayout"] = True

    # setting up data from csv file
    columns = ["DATE","PRCP","SNOW","SNWD","TAVG","TMAX","TMIN"]
    df = pd.read_csv("data/newCSV.csv", usecols=columns)

    # constructing sin curve based on input equation variables
    t = np.linspace(0, 730, num=200)
    amplitude = equation[0]
    frequency = 2*np.pi/365 # set so there is one cycle per year
    phase_angle = equation[1]
    vert_shift = equation[2]
    y1 = amplitude * np.sin(frequency*t + phase_angle) + vert_shift
    # Plotting data
    plt.plot(t, y1)
    plt.plot(df.DATE, df.TAVG)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=50))
    # Adding axis labels
    plt.xlabel('Date')
    plt.ylabel('Temperature (F)')
    # Adding title to graph
    plt.title('Sine Curve Over Weather Data')
    plt.show()