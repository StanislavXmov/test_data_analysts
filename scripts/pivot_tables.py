import pandas as pd

df = pd.read_csv('./datas/Data.csv')
print(df)

def get_max(df):
  df = df.drop(['Advertising', 'Size'], axis=1).agg('max')
  return df

def get_max_for_category(df):
  df = df.groupby(['Advertising']).agg(['max'])
  return df

def get_median_for_category(df):
  df = df.drop(['Advertising'], axis=1).groupby(['Size']).agg(['median'])
  return df

print(get_max(df))
print(get_max_for_category(df))
print(get_median_for_category(df))