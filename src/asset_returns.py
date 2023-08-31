import pandas as pd

def calculate_asset_returns(data):
    """
    Calculate asset returns based on close prices.

    Parameters:
        data (DataFrame): DataFrame containing historical data for assets.

    Returns:
        asset_returns (DataFrame): DataFrame with asset return columns.
        cumulative_returns (DataFrame): DataFrame with asset cumulative return columns.
    """

    # Calculate percent returns for each asset
    asset_returns = data.pct_change()

    # Rename columns to indicate returns
    asset_returns.columns = [f'{col} Returns' for col in asset_returns.columns]

    # Calculate cumulative returns for each asset
    cumulative_returns = (1 + asset_returns).cumprod()

    # Rename columns to indicate cumulative returns
    cumulative_returns.columns = [f'{col} Cumulative Returns' for col in data.columns]

    return asset_returns, cumulative_returns





