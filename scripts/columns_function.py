import pandas as pd

df_clicks = pd.read_csv('./datas/Cite_clicks.csv', index_col=0)

def change_type(df):
  df.fillna(df.mean(), inplace=True)
  df['SHOP1'] = df['SHOP1'].astype(int)
  return df

def get_clicks_statistic(df):
  df.fillna(df.mean(), inplace=True)
  df['CLICKS_STATISTIC'] = df['SHOP1'].apply(lambda x: 1 if x >= 200 else 0)
  return df

def change_statistic(df):
  df = get_clicks_statistic(df)
  map_dict = {0:'bad', 1:'good'}
  df["CLICKS_STATISTIC"] = df["CLICKS_STATISTIC"].map(map_dict)
  return df

# df = change_type(df_clicks)
# print(df[['SHOP1', 'SHOP2']])
# clicks_statistic = get_clicks_statistic(df_clicks)
# clicks_statistic_map = change_statistic(df_clicks)
# print(clicks_statistic_map)

# print(get_clicks_statistic(df_clicks))

df = get_clicks_statistic(df_clicks)
print(df)