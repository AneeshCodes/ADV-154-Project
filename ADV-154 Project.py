# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:46:58 2022

@author: anees
"""

import matplotlib.pyplot as plt

data = [[1,2,3,4,5,6,7,8,9,10]]
data = [
        [10,10,10,10,10,10,10,10,10,10,5,10,10,10],
        [10,10,10,10,10,10,10,10,10,9,6,5,10,10],
        [10,10,10,10,10,10,10,10,9,9,9,6,5,10],
        [10,10,10,10,10,10,10,9,9,1,9,9,6,5],
        [10,10,10,10,10,10,9,9,9,9,9,9,6,5],
        [10,10,10,10,10,9,9,9,9,1,9,9,6,5],
        [10,10,10,10,9,9,9,9,9,9,9,6,5,5],
        [10,10,10,9,9,9,9,1,9,9,9,6,5,5],
        [10,10,9,1,9,1,9,9,9,9,6,5,5,10],
        [10,5,6,9,9,9,9,9,9,9,6,5,10,10],
        [10,10,5,6,6,6,6,6,6,6,5,10,10,10],
        [10,10,10,5,5,5,5,5,5,5,10,10,10,10]
]

plt.imshow(data, cmap="nipy_spectral")
plt.show()