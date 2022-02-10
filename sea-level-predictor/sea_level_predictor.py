import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(nrows = 1, ncols = 1)

    ax.scatter(
        data = df,
        x = 'Year',
        y = 'CSIRO Adjusted Sea Level'
    )

    # Create first line of best fit
    line = lambda a, b, x: a * x + b
    years = range(1880, 2050 + 1)
    first_linreg = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    ax.plot(
        years,
        line(first_linreg.slope, first_linreg.intercept, years)
    )

    # Create second line of best fit
    recent_data = df['Year'] >= 2000
    years = range(2000, 2050 + 1)
    second_linreg = linregress(
        df[recent_data]['Year'],
        df[recent_data]['CSIRO Adjusted Sea Level']
    )

    ax.plot(
        years,
        line(second_linreg.slope, second_linreg.intercept, years)
    )

    # Add labels and title
    ax.set(
        title = 'Rise in Sea Level',
        xlabel = 'Year',
        ylabel = 'Sea Level (inches)'
    )
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

