import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # --------------------------
    # 1. Line of best fit (ALL data)
    # --------------------------
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Extend line to 2050
    years_extended = pd.Series(range(1880, 2051))
    line_all = res.slope * years_extended + res.intercept

    plt.plot(years_extended, line_all, 'r', label='Fit: All Data')

    # --------------------------
    # 2. Line of best fit (from 2000)
    # --------------------------
    df_recent = df[df['Year'] >= 2000]

    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    years_recent = pd.Series(range(2000, 2051))
    line_recent = res_recent.slope * years_recent + res_recent.intercept

    plt.plot(years_recent, line_recent, 'g', label='Fit: 2000 onwards')

    # Labels & title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.legend()

    # Save plot
    plt.savefig('sea_level_plot.png')

    return plt.gca()


# Run for testing
if __name__ == "__main__":
    draw_plot()
    plt.show()