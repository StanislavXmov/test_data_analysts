import os
import pandas as pd

# './data/Orders.xlsx'
orders_path = './datas/Shop_orders.csv'
        
def rename_columns(df):
    df.columns = [f'shop_{i}' for i in range(1, len(df.columns) + 1)]

def fillna_values(df, value=0):
  return df.fillna(value)

def etl(orders_path):
  # df = pd.read_excel(orders_path)
  # df = fillna_values(df, 1)
  # rename_columns(df)
  df = pd.read_csv(orders_path, index_col=0)
  df = fillna_values(df, 1)
  rename_columns(df)

  # df.to_csv(f"{path}Orders_etl.csv")
  # df.to_excel(f"{path}Orders_etl.xlsx")
  dir_path = '/'.join(orders_path.split('/')[:-1])

  etl_csv_path = os.path.join(dir_path, 'Orders_etl.csv')
  etl_xlsx_path = os.path.join(dir_path, 'Orders_etl.xlsx')
  print(etl_csv_path)
  print(etl_xlsx_path)

  # df.to_csv(etl_csv_path)
  # df.to_excel(etl_xlsx_path)

etl(orders_path)