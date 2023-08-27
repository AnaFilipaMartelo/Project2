import pandas as pd

def remove_nan(data_df):
    """
    Remove rows containing any NaN values from the given DataFrame.

    Parameters:
        data_df (DataFrame): The DataFrame to remove rows with NaN values from.

    Returns:
        DataFrame: The DataFrame with rows containing NaN values removed.
    """
    cleaned_df = data_df.dropna(axis=0, how='any')

    return cleaned_df






