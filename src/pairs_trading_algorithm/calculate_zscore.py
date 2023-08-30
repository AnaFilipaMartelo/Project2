
import numpy as np

def calculate_zscore(spread):
    """
    Calculate the z-score of a given spread value.

    Parameters:
        spread (Pandas Series): The spread value.

    Returns:
        z_score (Pandas Series): The calculated z-score.
    """
    mean_spread = spread.mean()
    std_dev_spread = spread.std()
    z_score = (spread - mean_spread) / std_dev_spread
 
    return z_score

