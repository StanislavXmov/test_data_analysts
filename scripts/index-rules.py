import pandas as pd

def read_data(path):
    # df = pd.read_excel(path, skiprows=2)
    df = pd.read_excel(path)
    return df.fillna(0)

df = read_data('./datas/Orders.xlsx')
print(df)

def set_index(df):
    # df.index = [f'UUID_{i}' for i in range(1, len(df) + 1)]
    l = []
    idxs = range(1, df.index.stop + 1, 1)
    for i in idxs:
        l.append(f"UUID_{i}")
    df.index = l
    return df

def rename_indexes(df, name='UUID_indexes'):
    df.index.name = name
    return df

def get_rows(df, rows=5):
    return df.iloc[0: rows]



print(set_index(df))
print(rename_indexes(df, 'test'))
print(get_rows(df, 2))