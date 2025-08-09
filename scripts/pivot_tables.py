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

def calculate_retention(csv_data):
  df = pd.read_csv(csv_data)
  df['FirstVisitMonth'] = pd.to_datetime(df['FirstVisitDate']).dt.to_period('M')
  df['FollowUpVisitMonth'] = pd.to_datetime(df['FollowUpVisitDate']).dt.to_period('M')

  cohort_data = df.groupby(['FirstVisitMonth', 'FollowUpVisitMonth']).agg({'UserID': 'nunique'}).reset_index()
  cohort_counts = cohort_data.pivot_table(index='FirstVisitMonth', columns='FollowUpVisitMonth', values='UserID')

  for row in cohort_counts.index:
    first_non_zero = cohort_counts.loc[row].first_valid_index()
    cohort_counts.loc[row] = (cohort_counts.loc[row] / cohort_counts.loc[row, first_non_zero]).round(2).fillna(0)

  return cohort_counts

print(calculate_retention('./datas/visits.csv'))

# df = calculate_retention('./datas/visits.csv')
# df[:'2021-01'] = df.loc['2021-01'] + 10
# print(df)