import pandas as pd

df_clicks = pd.read_csv('./datas/Cite_clicks.csv', index_col=0)

def check_nan(df):
  # all = len(df) * len(df.columns)
  # not_nan = (~df.isna()).sum().sum()
  # return all - not_nan
  return df.isna().values.sum()

def read_with_nan(path, value):
    df = pd.read_csv(path, index_col=0)
    df = df.fillna(value)
    return df

def get_clean_df(path):
  df = read_with_nan(path, 0)
  # df = df.abs()
  # print(df)
  df = df.where(df >= 0, df.abs())
  return df


print(check_nan(df_clicks))
# print(check_nan(df_clicks[:2]))
clean_df = read_with_nan('./datas/Cite_clicks.csv', 0)
# print(check_nan(clean_df))
# print(get_clean_df('./datas/Cite_clicks.csv'))
clean_df = get_clean_df('./datas/Cite_clicks.csv')
print(clean_df)
# print((clean_df < 0).values.sum())