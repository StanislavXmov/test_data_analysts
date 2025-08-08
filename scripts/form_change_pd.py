import pandas as pd

df = pd.read_csv('./datas/Cite_clicks.csv', index_col=0)
# print(df)

# df1 = df[['SHOP1', 'SHOP2']][0:10]
# df2 = df[['SHOP3', 'SHOP4']][0:10]
df1 = df[['SHOP1', 'SHOP2']][19:25].reset_index()
df2 = df[['SHOP3', 'SHOP4']][5:20].reset_index()

def concat(df1, df2):
  return pd.concat([df1, df2], axis=1)


def join_intersect(df1, df2):
  return df1.join(df2, how='inner')

def merge_all(df1, df2):
  return pd.merge(df1, df2, left_on='day', right_on='day', how='outer')
    
# result_df = concat(df1, df2)
# result_df = join_intersect(df1, df2)
result_df = merge_all(df1, df2)

print(result_df)

def convert_to_xlsx(filepath_from: str, filepath_to: str, skiprows=None):
    df = pd.read_excel(filepath_from, skiprows=skiprows)
    df.to_excel(filepath_to, index=None)


def etl_max(filepath_from: str, filepath_to: str):
  df = pd.read_excel(filepath_from)
  df = df.fillna(0)
  # df_max = pd.DataFrame(df_orders.max()).T.round(1)
  # df_max.index = ['Max']
  # df = pd.concat([df, df_max])
  df_max = df.agg("max")
  df_max = pd.DataFrame([df_max])
  df = pd.concat([df, df_max])
  df.index = range(0, df.shape[0])
  df = df.rename(index={df.shape[0] - 1: "Max"})

  # with pd.ExcelWriter(filepath_to, engine="xlsxwriter", mode="w") as excel_writer:
  #     df.to_excel(excel_writer, sheet_name="All")
  #     print(df.columns.to_list())
  #     for shop_name in df.columns.to_list():
  #       df[[shop_name]].to_excel(excel_writer, sheet_name=shop_name)