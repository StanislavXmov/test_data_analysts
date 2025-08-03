import numpy as np

# grades_1 = [
#   [2, 2, 5, 3],
#   [3, 4, 2, 5],
#   [3, 5, 5, 4],
#   [4, 4, 5, 2],
#   [5, 5, 4, 5]]

# grades_2 = [[5, 3, 3, 5],
#             [4, 5, 4, 5],
#             [3, 2, 2, 2],
#             [3, 2, 2, 2],
#             [5, 2, 4,2]]


def better_in_subject(grades_1, grades_2, subject):
  subjects = {
    "Math": 0, "Chemistry": 1, "Physics": 2, "Literature": 3
  }
  np_grades_1 = np.array(grades_1)
  np_grades_2 = np.array(grades_2)
  if np_grades_1[:, subjects[subject]].mean() > np_grades_2[:, subjects[subject]].mean():
    return 1
  else:
    return 2

def get_above_average(grades_1, grades_2, group):
  np_grades_1 = np.array(grades_1)
  np_grades_2 = np.array(grades_2)
  np_all_grades = np.concatenate((np_grades_1, np_grades_2), axis=0).mean(axis=0)
  grade = np_grades_1
  if group == 2:
    grade = np_grades_2
  list = []
  for i in range(len(np_all_grades)):
    value = np_all_grades[i]
    percentile = np.searchsorted(np.sort(grade[:, i]), value, side='left') / len(grade[:, i]) * 100
    list.append(round(100 - percentile, 2))
  return list

# def get_above_average(grades_1, grades_2, group):
#     average_grades_by_subject = np.mean(np.concatenate((grades_1, grades_2)), axis=0)
#     print(np.array(grades_1 > average_grades_by_subject).mean(axis=0))
#     groups = {
#         1: np.round((grades_1 > average_grades_by_subject).mean(axis=0) * 100, 2),
#         2: np.round((grades_2 > average_grades_by_subject).mean(axis=0) * 100, 2)
#     }
#     return groups[group]

# print(better_in_subject(grades_1, grades_2, "Literature"))

# print(get_above_average(grades_1, grades_2, 1))
# print(get_above_average(grades_1, grades_2, 2))

def grades():
    np.random.seed(42)
    grades_group_1 = np.random.randint(2, 6, size=(15, 4))
    grades_group_2 = np.random.randint(2, 6, size=(15, 4))
    return grades_group_1, grades_group_2

grades_1, grades_2 = grades()

print(get_above_average(grades_1, grades_2, 1))
print(get_above_average(grades_1, grades_2, 2))