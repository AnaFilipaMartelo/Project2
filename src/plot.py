import pandas as pd
import hvplot.pandas
from bokeh.plotting import show

def plot_returns(data):
    """
    Create an interactive plot for cumulative returns using hvplot.

    Parameters:
        data (DataFrame): DataFrame containing cumulative returns data.

    Returns:
        returns_plot (hvplot plot object)
    """
    # Extract the common words from the column names while preserving order
    common_words = []
    for word in data.columns[0].split():
        if all(word in col for col in data.columns):
            common_words.append(word)

    # Convert the set back to a string
    common_title = ' '.join(word.title() for word in common_words)
        
    # Create the cumulative returns plot using hvplot
    returns_plot = data.hvplot.line(
        xlabel='Time', ylabel=common_title, title=common_title,
        line_width=2, alpha=0.7, hover_line_color='red',
        width=1000, height=500,
        legend='top_left'
    )

    # Show the plot using Bokeh
    return returns_plot