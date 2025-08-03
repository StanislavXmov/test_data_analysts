import numpy as np
import random
import collections

purchases = np.array([
   [1, 2, 5, 0, 0],
   [1, 1, 0, 1, 4],
   [0, 3, 0, 0, 1],
   [1, 5, 0, 0, 3]])


# BEGIN
def get_recommendation(data, user_id):
    similarity = np.corrcoef(data)
    similarity[user_id, user_id] = -np.inf
    similar_users = np.argsort(-similarity[user_id])[:5]

    recommendations = []

    for similar_user in similar_users:
        for item_id, count in enumerate(data[similar_user]):
            if count > 0 and data[user_id][item_id] == 0:
                recommendations.append(item_id)
    return [k for k, _ in collections.Counter(recommendations).most_common(3)]
# END

recs = get_recommendation(purchases, 0)

print(recs)