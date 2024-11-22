
# This File is to simply import raw data and do necessary formatting 
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

btc_df = pd.read_csv(
    '#Add the import file path')

#Transform Epoch Time to Formatted Time
btc_df['Time'] = pd.to_datetime(btc_df['Time'] / 1000, unit='s')


def get_data():
    return btc_df
