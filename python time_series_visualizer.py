import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    parse_dates=["date"],
    index_col="date"
)

# Clean data (remove top & bottom 2.5%)
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]


# =========================
# 1. LINE PLOT
# =========================
def draw_line_plot():
    df_line = df.copy()

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df_line.index, df_line['value'], color='red')

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig('line_plot.png')
    return fig


# =========================
# 2. BAR PLOT
# =========================
def draw_bar_plot():
    df_bar = df.copy()

    # Extract year & month
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar['month_name'] = df_bar.index.strftime('%b')

    # Group data
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    fig = df_grouped.plot(kind='bar', figsize=(10, 7)).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(
        title="Months",
        labels=[
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
        ]
    )

    fig.savefig('bar_plot.png')
    return fig


# =========================
# 3. BOX PLOT
# =========================
def draw_box_plot():
    df_box = df.copy().reset_index()

    # Add columns
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # Sort months
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Year-wise box plot
    sns.boxplot(
        x='year',
        y='value',
        data=df_box,
        ax=axes[0]
    )
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(
        x='month',
        y='value',
        data=df_box,
        order=month_order,
        ax=axes[1]
    )
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig('box_plot.png')
    return fig


# =========================
# RUN
# =========================
if __name__ == "__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
    plt.show()