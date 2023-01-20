import matplotlib.pyplot as plt
import numpy as np
"""
#適当なデータセットを作成する
np.random.seed(0)
points1 = np.random.randn(80, 2)
#points2 = np.random.randn(80, 2) + np.array([4,0])
#points3 = np.random.randn(80, 2) + np.array([5,8])
#print(points1)
#print(points2)
#print(points3)
#points = np.r_[points1, points2, points3]
#np.random.shuffle(points)
"""
a = np.array([356], dtype = "int16")
print(a.nbytes, a)
#bit_a = np.array([bin(a[i]) for i in a])
#print(bit_a.nbytes, bit_a)
a.dtype = "int8"
print(a.nbytes, a)