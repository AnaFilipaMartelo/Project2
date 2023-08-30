import pandas as pd

def count_pairs_signals(signals_dict):
    """
    Count the occurrences of different types of trading signals for pairs of assets and organize the results
    in a legible DataFrame format.

    Parameters:
        signals_dict (dict): Dictionary containing trading signals for each identified pair.

    Returns:
        df (DataFrame): DataFrame with the counts of buy (1), sell (-1), and no signal (0) for each asset pair.
    """

    signal_counts = {}
    
    for pair, signals in signals_dict.items():
        counts = {"1": 0, "-1": 0, "0": 0}
        
        for signal in signals:
            counts[str(signal)] += 1
        
        signal_counts[pair] = counts
    
    # Create a DataFrame directly from the signal_counts dictionary
    df = pd.DataFrame.from_dict(signal_counts, orient='index')
    # Set the index names
    df.index.names = ['Asset 1', 'Asset 2'] 
    df.reset_index(inplace=True)

    return df