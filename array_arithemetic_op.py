import numpy as np
# addition,substraction..

# a = np.array([i for i in range(1,11)])

# print(a)       # [ 1  2  3  4  5  6  7  8  9 10]

# print(a.reshape((2,5)))     #[[ 1  2  3  4  5]
#  #                            [ 6  7  8  9 10]]

# b = np.arange(1,9).reshape(2,4).ndim

# print(b)        # 2

# b = np.array([[1,2,3,4],[5,6,7,8]])

# print(b.flatten())      #[1 2 3 4 5 6 7 8]

# a = np.array([[3,2,4,1],[6,4,3,1]])
# b = np.array([[1,2,3,4],[5,6,7,8]])

# print(a)            #[[3 2 4 1]
#    #                  [6 4 3 1]]

# print(b)            #[[1 2 3 4]
# #                     [5 6 7 8]]

# print(np.add(a,b))      #[[ 4  4  7  5]
# #                         [11 10 10  9]]

# print(a+b)          #[[ 4  4  7  5]
# #                     [11 10 10  9]]

# print(np.subtract(a,b))     # [[ 2  0  1 -3]
# #                              [ 1 -2 -4 -7]]

# print(np.multiply(a,b))        #[[ 3  4 12  4]
# #                                [30 24 21  8]]

# print(np.divide(a,b))           #[[3.         1.         1.33333333 0.25      ]
# #                                 [1.2        0.66666667 0.42857143 0.125     ]]

# print(np.square(a))         #[[ 9  4 16  1]
# #                             [36 16  9  1]]

# print(np.sqrt(a))           #[[1.73205081 1.41421356 2.         1.        ]
# #                             [2.44948974 2.         1.73205081 1.        ]]


# a = np.array([[3,2,4,1],[6,4,3,1]])

# a * 2 # each element in array has been multyiply with 2 and return result in a array
# a ** 2 # vector calculation
# a / 2
# # return sum of all elements in the array

# print(np.sum(a,axis=None)) #24

# print(np.sum(a,axis=1)) # sum of elements in rowise >>> [10 14]

# print(np.sum(a,axis=0)) #[9 6 7 2] sum of elements in columnwise

# # sorting
#   -------
# rev = np.sort(a)    # ascending order rowise
# print(rev)      # [[1 2 3 4]
#  #                 [1 3 4 6]]
# print(np.sort(a)[:,::-1]) # decending order rowise
# #                   [[4 3 2 1]
# #                    [6 4 3 1]]       




# arr_2 = np.array([4,3,5,7,2,10])
# print(arr_2.argmax())       # 5     # ascending order
# print(arr_2.argmin())       # 4
# print(arr_2.argsort())      # [4 1 0 2 3 5]

# rev = np.sort(a,axis=1)[:,::-1]  # decending order in rowise
# print(rev)      #[[4 3 2 1]
# #                 [6 4 3 1]]

# rev = np.sort(a,axis=0)[::-1,:]  # decending order in columnwise
# print(rev)      #[[6 4 4 1]
# #                 [3 2 3 1]]


# """
# col_index     0   1   2   3
#             [[1   2   3   4]   -> 0
#              [5   6   7   8]   -> 1
#              [9  10  11  12]   -> 2
#              [13 14  15  16]   -> 3
#              [17 18  19  20]]  -> 4    row_index

# """
# arr = np.arange(1,21).reshape(5,4)
# print(arr)

# print(arr[1:3,1:3])  #[[ 6  7]
# #                      [10 11]] 

# print(arr[2:4,1::])   #[[10 11 12]
#  #                      [14 15 16]]

# print(arr[1:4,2::])    #[[ 7  8]
#  #                       [11 12]
#  #                       [15 16]]

# print(arr[1:4,0:2])     #[[ 5  6]
#  #                        [ 9 10]
#  #                        [13 14]]

# arr2 = np.array([
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ])

# print(arr2.argmax()) # 11 returns the index after flatten the 2-d arrey
# print(arr2.argmax(axis=0))      # [2 2 2 2]
# print(arr2.argmax(axis=1))      # [3 3 3]
# print(arr2.argmin(axis=0))      # [0 0 0 0]
# print(arr2.argmin(axis=1))      # [0 0 0]

# where
# -----

# arr_2 = np.array([4,3,5,7,2,10])

# print(np.where(arr_2 > 5))     #(array([3, 5]),)
# #                                        row index                     column index
# #                                            !                               !
# print(np.where(arr2 > 5))      # (array([1, 1, 1, 2, 2, 2, 2]), array([1, 2, 3, 0, 1, 2, 3]))

# print(np.where(arr_2 > 5,"pass","fail"))        # ['fail' 'fail' 'fail' 'pass' 'fail' 'pass']

# arr = np.array([[30,10,90],
#                 [20,40,70],
#                 [25,45,80]])

# print(arr[::-1,:])
# """
# [[25 45 80]
#  [20 40 70]
#  [30 10 90]]

#  it reverse all the rows by selecting all the column
# """
# print(arr[:,::-1])
# """
# [[90 10 30]
#  [70 40 20]
#  [80 45 25]]
 
#  it selects all the rows and reverse the column
# """
# print(arr[0:2,::-1])
# """
# [[90 10 30]
#  [70 40 20]]

# it selects first two rows and reverse the column
# """
# print(arr[::-1,::-1])
# """
# [[80 45 25]
#  [70 40 20]
#  [90 10 30]]

#  it reverse all the rows and column
# """

# print(np.sort(arr))       # default is row so it will sort ascending order rowise
# print(np.sort(arr)[:,::-1])     # it will sort in reverse by column wise
# print(np.sort(arr)[::-1,::-1])   # it will sort columnwise and rowise

# print(np.sort(arr,axis=0)) # it will sort the column in ascending order

# arr_3 = np.array([4.65,5.35,6.98,7.5])

# print(np.floor(arr_3))  # [4. 5. 6. 7.]
# print(np.round(arr_3))  # [5. 5. 7. 8.]
# print(np.ceil(arr_3))   # [5. 6. 7. 8.]

# print(arr_3.size)       # 4
 