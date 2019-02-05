import pandas as pd

def simple_moving_average(df, asset_price, sma, n):
    """
    Simple Moving Average (SMA) is an arithmetic moving average calculated by
    adding recent closing prices then dividing that by the number of time periods
    in the calculation average.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset price.
        asset_price (string): the column name of the price of the asset.
        sma (string): the column name for the n-day moving average results.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with n-day moving average of the asset calculated.

    """

    df[sma] = df[asset_price].rolling(window=n).mean()

    return df
