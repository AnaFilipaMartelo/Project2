import pandas as pd

def calculate_strategy_returns(data, signals_dict, pairs):
    """
    Calculate strategy returns based on trading signals.

    Parameters:
        data (DataFrame): DataFrame containing historical data for assets and returns.
        signals_dict (dict): Dictionary containing trading signals for each identified pair.
        pairs (list): List of pairs of assets.

    Returns:
        merged_data (DataFrame): DataFrame with calculated strategy returns.
    """
    strategy_returns = pd.DataFrame(index=data.index)

    for asset1_col, asset2_col in pairs:

        # Retrieve the signals array for the current pair
        signals = signals_dict[(asset1_col, asset2_col)] 
        
        # Calculate the returns for the trading strategy based on the signals
        strategy_returns[f'{asset1_col}, {asset2_col} Strategy Returns'] = (
            data[f'{asset1_col} Returns'] * signals +
            data[f'{asset2_col} Returns'] * -signals
        )

        # Calculate the cumulative strategy returns
        strategy_returns[f'{asset1_col}, {asset2_col} Cumulative Strategy Returns'] = (
            1 + strategy_returns[f'{asset1_col}, {asset2_col} Strategy Returns']
        ).cumprod()

    return strategy_returns






