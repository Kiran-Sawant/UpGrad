import numpy as np

height: list[int] = [[74], [2], [3]]
weight: list[int] = [[54, 64, 57]]

np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)
print(np_weight)
# print(np_height.shape)

print(np_height + np_weight)