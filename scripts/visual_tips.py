import pandas as pd
import matplotlib.pyplot as plt

df_clicks = pd.read_csv('./datas/Cite_clicks.csv', index_col=0)

def read_and_plot(path):
  df = pd.read_csv(path, index_col=0)
  df.plot()
  plt.show()

def clean_plot(path):
  df = pd.read_csv(path, index_col=0)
  df = df[df > 200]
  df = df.fillna(df.min().min())
  # mask = (df > 0)
  # min_value = df[mask].dropna().values.min()
  # df = df.where(mask, min_value)
  df.plot()
  plt.show()

def max_plot(path):
  df = pd.read_csv(path, index_col=0)
  mask = (df > 0)
  min_value = df[mask].dropna().values.min()
  df = df.where(mask, min_value)
  df.max().plot(kind="pie")
  plt.show()

clean_plot('./datas/Cite_clicks.csv')