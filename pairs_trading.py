import numpy as np
from itertools import combinations
from calculate_zscore import calculate_zscore

def find_pairs_signals(tickers, data, zscore_threshold):
    """
    Find pairs of assets based on z-score thresholds and calculate trading signals.

    Parameters:
        tickers (list): List of asset tickers.
        data (DataFrame): DataFrame containing historical data for each asset.
        zscore_threshold (float): Threshold for z-score to identify pairs.

    Returns:
        pairs (list): List of pairs of assets that satisfy the z-score condition.
        signals (dict): Dictionary of trading signals for each identified pair.
    """
    # Initialize pairs list
    pairs = []
    signals = {}
    
    # Generate all possible combinations of 2 assets
    asset_combinations = combinations(tickers, 2)
    
    for asset1, asset2 in asset_combinations:
        # Access the close prices for each asset directly from the data DataFrame
        data1 = data[asset1]
        data2 = data[asset2]
        # Calculate spread
        spread = data1 - data2  
        zscore = calculate_zscore(spread)
        
        if (abs(zscore) > zscore_threshold).any():
            pairs.append((asset1, asset2))
	        # Generate buy and sell signals for the pair based on z-score
            # If z-score > zscore_threshold, suggests a sell signal (short asset1, long asset2)
            # If z-score < -zscore_threshold, suggests a buy signal (long asset1, short asset2)
            # If neither condition is met, no signal is generated (signals = 0)
            signals[(asset1, asset2)] = np.where(zscore > zscore_threshold, -1, np.where(zscore < -zscore_threshold, 1, 0)) 
    
    return pairs, signals
