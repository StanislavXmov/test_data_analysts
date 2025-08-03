import numpy as np

days = [12, 16, 20, 32, 24, 22, 12, 18]

def moving_average(data, window_size):
  window = np.ones(window_size) / window_size
  return np.convolve(data, window, 'same')

# print(moving_average(days, 5))
# print(moving_average(days, 5).mean())

def anomalous_days_count(temperatures):
  arr = np.array(temperatures)
  window = np.ones(5) / 5
  convolve = np.convolve(arr, window, 'valid')
  diff = np.abs(arr[4:] - convolve)
  return np.sum(diff >= 5)

def stable_days_count(temperatures):
  arr = np.array(temperatures)
  window = np.ones(5) / 5
  convolve = np.convolve(arr, window, 'valid')
  diff = np.abs(arr[4:] - convolve)
  return np.sum(diff < 2)

def max_stable_period(temperatures):
  arr = np.array(temperatures)
  window = np.ones(5) / 5
  convolve = np.convolve(arr, window, 'valid')
  diff = np.abs(arr[4:] - convolve)
  c = 0
  c_max = 0
  i = False
  for d in diff:
    if d < 2:
      if i == False:
        i = True
        c += 1
        if c > c_max:
          c_max = c
      else:
        c += 1
        if c > c_max:
          c_max = c
    else:
      i = False
      c = 0
  return c_max


# BEGIN
# def moving_avg(x, n):
#     cumsum = np.cumsum(np.insert(x, 0, 0))
#     return (cumsum[n:] - cumsum[:-n]) / float(n)


# def find_temperatures_diff(temperatures):
#     moving_average = moving_avg(temperatures, 5)
#     # дополняем массив nan для сопоставления с исходным массивом температур
#     extended_moving_average = np.concatenate((np.full(4, np.nan), moving_average))
#     temperatures_diff = np.abs(temperatures - extended_moving_average)
#     return temperatures_diff


# def anomalous_days_count(temperatures):
#     temperatures_diff = find_temperatures_diff(temperatures)
#     anomalies = temperatures_diff >= 5
#     anomalous_days_count = np.sum(anomalies)
#     return anomalous_days_count


# def stable_days_count(temperatures):
#     temperatures_diff = find_temperatures_diff(temperatures)
#     stable_days = temperatures_diff <= 2
#     stable_days_count = np.sum(stable_days)
#     return stable_days_count


# def max_stable_period(temperatures):
#     temperatures_diff = find_temperatures_diff(temperatures)
#     stable_days = temperatures_diff <= 2

#     change_points = np.where(np.logical_not(stable_days))[0] + 1
#     all_points = np.concatenate(([0], change_points, [len(temperatures)]))

#     stable_periods = np.diff(all_points) - 1
#     return np.max(stable_periods)
# # END

print(anomalous_days_count(days))
print(stable_days_count(days))
print(max_stable_period(days))