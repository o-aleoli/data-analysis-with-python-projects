from matplotlib import figure
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    "./fcc-forum-pageviews.csv",
    sep = ",",
    header = 0,
    index_col = 0,
    parse_dates = ["date"]
)

# Clean data
df = df[
    (df["value"] > df["value"].quantile(0.025)) &\
    (df["value"] < df["value"].quantile(0.975))
]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (32, 10))
    ax.plot(
        df,
        color = "red"
    )
    ax.set(
        title = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
        xlabel = "Date",
        ylabel = "Page Views"
    )

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Months"] = df_bar.index.strftime("%B")
    df_bar["Years"] = df_bar.index.year
    df_bar = df_bar.groupby(['Years', 'Months'])['value'].mean().unstack()
    df_bar = df_bar.rename(columns = {"value": "Average Page Views"})\
        .reset_index()

    # Draw bar plot

    labels = ['January','February','March','April','May','June','July','August','September','October','November','December']

    fig = df_bar.plot(kind='bar',x='Years').figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title = "Months", labels = labels)
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Copy and modify data for monthly bar plot
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    labels = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    fig, axs = plt.subplots(ncols = 2, nrows = 1, sharex = False)

    sns.boxplot(
        data = df_box,
        x = "year",
        y = "value",
        ax = axs[0]
    )\
    .set(
        title = "Year-wise Box Plot (Trend)",
        xlabel = "Year",
        ylabel = "Page Views"
    )

    sns.boxplot(
        data = df_box,
        x = "month",
        y = "value",
        order = labels,
        ax = axs[1]
    )\
    .set(
        title = "Month-wise Box Plot (Seasonality)",
        xlabel = "Month",
        ylabel = "Page Views"
    )

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

