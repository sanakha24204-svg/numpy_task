"""
EDA (Exploratory data analysis)
-----------------------------

> EDA is the analysing the different datasets to understand its patterns
  which can be termed as datahandling, data manipulation etc...

> Used to analyse the data from different datasets using 4 different python libraries.

(numpy,pandas,matplotlip,seaborn) - libraries

jupyter notebook
google collab

package - which has more than one module
==================================================================================================================================

#                                            STEPS
*                                           -------

* Identifying the problem ---> collecting thr data(dataset) --->      Pandas            --->       Numpy
#                                                                Analysing the dataset         Get the analysed data
#                                                                    analysing                   numerical format
#                                                                   missing vaues
#                                                                 removing the noise
#                                                                   filling values

                                                                    
* ---> used to train  ---> Evaluation and deployment
#      the model(ML)

===================================================================================================================================

<> numpy(numerical python)
   -----------------------

    Used to numerical and mathematical operations
    In numpy array is used as collection becuz it is faster than python list
    It is a full of methods
    It is much faster than list
    
> array
  -----

  Array can be considered as collection of element.

  It is a collection of more than one values
  It is homogeneous(doesn't allow more than one datatype in it)
  It is a vector based calculation(matrix based)
  It has no iteration(in list)

  
if u want to call numpy use np
to find dimention (elements.ndim)

> One dimentional array
  ---------------------

  array contains a single row of elements it can be termed as 1-dimentional array

> Two dimentional array
  --------------------

  array contains two rows of elements(rows and columns) (table like format)

  np.array([[row1],[row2]])

> Three dimentional array
  -----------------------
  
  An array contains more than one 2 dimentional array can be ter,ed as 3-d array

  np.array([])



if it is an attribute it do not give brackets

print(elements.ndim) - to know the dimention of the array
print(element.dtype) - to know the datatype of the element
print(element.shape) - it shows no of dimentions , no of rows in each array,no of column
print(a.reshape((2,5))) - to convert to two dimention array
print(b.flatten())    - converting 2-d/3-d array into i-d array
a * 2 # each element in array has been multyiply with 2 and return result in a array
a ** 2 # vector calculation
a / 2
print(np.add(a,b)
print(a+b) 
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
print(np.square(a))
print(np.sqrt(a))
# return sum of all elements in the array
  ---------------------------------
print(np.sum(a,axis=None)) - (24)
print(np.sum(a,axis=1)) -  sum of elements in rowise >>> [10 14]
print(np.sum(a,axis=0))  - [9 6 7 2] sum of elements in columnwise

sorting in array
----------------
Arrange the element in acending or decending order
r = np.sort(a)    - ascending order
print(r)
r = np.sort(a,axis=1)[:,::-1]   - desending order
np.sort() - returns the array in ascending order
np.sort(a,axis=1)[:,::-1]  - in desending order
we are using slicing technique so need to give row index and column index
arr_2.argsort() - it returns the index position of ascending order
arr_2.argmax() - return the index value of the maximum value of an array
arr_2.argmin() - return the index value of the minimum value of an array 

slicing
-------

arr[row_start:row_stop:step,col_start:col_stop:step]


Types of matrices
-----------------

> Zero matrix   - matrix having all elements as zero
  m_1 = np.zeros((3,4)dtype= int)
  zero metrix having 3 rows and 4 columns with integer datatype

> ones matrix  - matrix having all element as 1
  m_2 = np.ones((4,3),dtype= int)

> full matrix 
  np.full(shape,value,dtype)
  print(np.full((3,4),5,dtype= int))

> Identity matrix  - rows and columns should be equal

  print(np.identity(n- 3,dtype= int))
  print(np.eye(N=4,dtype= int))

conditions
==========

> where
  -----

* It used to positioning the elements which satisfy the condition

np.where(condition) - used to positioning the elements which satisfy the condition

eg: print(np.where(arr2 > 5))

* It replace the elements from the array those stisfy the condition

np.where(condition,value_if_true,value_if_false)

eg: print(np.where(arr2 > 5,"pass","fail"))


"""
