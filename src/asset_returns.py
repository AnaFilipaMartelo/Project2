import pandas as pd

def calculate_asset_returns(data):
    """
    Calculate asset returns based on close prices.

    Parameters:
        data (DataFrame): DataFrame containing historical data for assets.

    Returns:
        data_with_returns (DataFrame): DataFrame with added asset return columns.
    """
    # Calculate percent returns for each asset
    asset_returns = data.pct_change()

    # Rename columns to indicate returns
    asset_returns.columns = [f'{col} Returns' for col in asset_returns.columns]

    # Concatenate the asset returns DataFrame with the original data
    data_with_returns = pd.concat([data, asset_returns], axis=1)

    return data_with_returns





