import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")

# Clean data
max=df['value'].max()
df = df[df['value'].between(df['value'].quantile(0.025), df['value'].quantile(0.975))]

df['date'] = pd.to_datetime(df['date'])
  # Copy and modify data for monthly bar plot
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month


def draw_line_plot():

    fig, ax = plt.subplots(figsize=(12, 6))
    # Draw line plot
    sns.lineplot(x=df.date,y=df.value,color='red')
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
  
    fig, ax = plt.subplots(figsize=(12, 6))
    # Draw bar plot

    sns.barplot(x='year', y='value', hue='month', data=df,palette='Set1',errorbar=None)


    plt.xlabel('Years')  
    plt.ylabel('Average Page Views')  
    plt.legend(title='Months', loc='upper left', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])  
    ax.tick_params(axis='x', rotation=90)


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df.sort_values(by='month',inplace=True)
    
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))
    # Draw box plots (using Seaborn)
    sns.boxplot(x='year', y='value', data=df_box,hue='year',ax=axes[0],fliersize=1,palette='Set1',legend=False)
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')


    sns.boxplot(x='month', y='value', data=df_box,ax=axes[1],fliersize=1,palette='Set2',legend=False)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
    


