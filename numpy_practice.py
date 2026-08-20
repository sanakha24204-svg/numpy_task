import numpy as np

elements = np.array([1,2,3,4])

print(elements)   #[1 2 3 4]

print(elements.ndim)  # 1  one dimentional

element_2 = np.array([[1,2,3,4],[5,6,7,8]])  

print(element_2)      # [[1 2 3 4]
                      #  [5 6 7 8]]

print(element_2.ndim)   # 2  two dimentional 

element_3 = np.array ([
            [[1,2,3],[4,5,6]],
            [[1,2,3],[4,5,6]],
            [[1,2,3],[4,5,6]]
])

print(element_3)  # [[[1 2 3]
 #                  [4 5 6]]

 #                  [[1 2 3]
 #                   [4 5 6]]

 #                  [[1 2 3]
  #                 [4 5 6]]]

print(element_3.ndim)   # three dimentional

print(element_2.shape) # (2,4)# indicates it has 2 rows and 4 columns
print(element_3.shape) # (3,2,4)

# zero based matrix
# -----------------

m_1 = np.zeros((3,4),dtype= int)
print(m_1) # float64
"""
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
"""

# one matrix
# ----------

m_2 = np.ones((4,3),dtype= int)
print(m_2)
"""
[[1 1 1]
 [1 1 1]
 [1 1 1]
 [1 1 1]]
"""

# full matrix
# -----------

print(np.full((3,4),5,dtype= int))
"""
[[5 5 5 5]
 [5 5 5 5]
 [5 5 5 5]]
"""

# Identity matrix

print(np.identity(n= 3,dtype= int))
"""
[[1 0 0]
 [0 1 0]
 [0 0 1]]
"""
print(np.eye(N=4,dtype= int))
"""
[[1 0 0 0]
 [0 1 0 0]
 [0 0 1 0]
 [0 0 0 1]]
 
"""