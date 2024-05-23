import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import numpy as np


def visualizedata(equation):
    plt.rcParams["figure.figsize"] = [15.00, 7]
    plt.rcParams["figure.autolayout"] = True
    columns = ["DATE","PRCP","SNOW","SNWD","TAVG","TMAX","TMIN"]
    df = pd.read_csv("data/newCSV.csv", usecols=columns)

    t = np.linspace(0, 730, num=200)
    amplitude = equation[0]
    frequency = 2*np.pi/365
    phase_angle = equation[1]
    vert_shift = equation[2]

    y1 = amplitude * np.sin(frequency*t + phase_angle) + vert_shift
    plt.plot(t, y1)
    plt.plot(df.DATE, df.TAVG)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=50))
    plt.show()

def main():
    visualizedata()

if __name__ == "__main__":
    main()