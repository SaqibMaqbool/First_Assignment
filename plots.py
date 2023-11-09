import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('WLD_RTFP_country_2023-10-02.csv')

# Convert the 'date' column to a datetime type if it's not already
df['date'] = pd.to_datetime(df['date'])

# Filter the DataFrame for Afghanistan
afghanistan_data = df[df['country'] == 'Afghanistan']

# Create a line plot for stock prices over time with a limited set of date labels
def create_line_plot(df, x_column, y_columns, labels, title):
    plt.figure(figsize=(10, 6))
    for i in range(len(y_columns)):
        plt.plot(df[x_column], df[y_columns[i]], label=labels[i])
    plt.xlabel(x_column)
    plt.ylabel("Values")
    plt.title(title)
    plt.xticks(df[x_column].iloc[::int(len(df) / 10)], rotation=45)
    plt.legend()
    plt.show()


create_line_plot(afghanistan_data, 'date', ['Open', 'High', 'Low', 'Close'], ['Open', 'High', 'Low', 'Close'], 'Stock Prices for Afghanistan Over Time')

# Bar Chart
def create_bar_chart(df, x_column, y_column, title):
    plt.figure(figsize=(16, 6))
    plt.bar(df[x_column], df[y_column])
    plt.xlabel(x_column)
    plt.ylabel("Values")
    plt.title(title)
    plt.xticks(rotation=90)
    plt.show()


create_bar_chart(df, 'country', 'Inflation', 'Inflation by Country')


# Creating a scatter plot with color based on 'Inflation'
def create_scatter_plot(df, x_column, y_column, color_column, title):
    plt.figure(figsize=(10, 6))
    
    # Define color map based on 'Inflation' values
    colormap = plt.cm.get_cmap('viridis')
    norm = plt.Normalize(df[color_column].min(), df[color_column].max())
    
    plt.scatter(df[x_column], df[y_column], c=df[color_column], cmap=colormap, norm=norm)
    cbar = plt.colorbar()
    cbar.set_label(color_column)
    
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(title)
    plt.show()


create_scatter_plot(df, 'Open', 'Close', 'Inflation', 'Open vs. Close Scatter Plot with Inflation Color')

