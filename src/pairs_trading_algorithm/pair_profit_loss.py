import pandas as pd

def calculate_pair_profit_loss(pairs, cumulative_strategy_returns, initial_investment, shares_size):
    """
    Calculate profit/loss for each pair based on trading signals.

    Parameters:
        pairs (list): List of pairs of assets.
        cumulative_strategy_returns (DataFrame): DataFrame with calculated cumulative strategy returns.
        initial_investment (float): Initial investment amount.
        shares_size (float): Number of shares or contracts to buy/sell for each trade.

    Returns:
        profit_loss (DataFrame): DataFrame with calculated profit/loss for each pair.
    """
    profit_loss = pd.DataFrame(index=cumulative_strategy_returns.index)
    
    for asset1_col, asset2_col in pairs:
        # Extract the cumulative strategy returns for the specific pair
        pair_cumulative_returns = cumulative_strategy_returns[f'{asset1_col}, {asset2_col} Cumulative Strategy Returns']
        
        # Calculate the value of the portfolio for each time period
        portfolio_value = initial_investment * (1 + pair_cumulative_returns * shares_size)
        
        # Calculate profit/loss relative to the initial investment
        profit_loss[f'{asset1_col}, {asset2_col} Profit/Loss'] = portfolio_value - initial_investment
    
    return profit_loss