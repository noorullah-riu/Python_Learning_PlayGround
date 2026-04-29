
# In Terminal go to file path cd and then (python model.py) run this command or
# In vs code right top click run 

#   Numpy in python curse notes
#   Def => Numpy is python based library which allows multi dimenssion arrays operations
#  and more scintific operation init

# Array VS List 
#Array is faster Array=[1 2 3 4]
# Takes less memory  list= [1,2,3,4]

#Installing NUMPY
# pip install numpy 

import numpy as NP

arrayX= NP.array([1,2,3,4]);
print(arrayX,'Printng Array');
print(type(arrayX),'type of arrayX')

listY=[1,2,3,4]
print(listY,'Printng List');
print(type(listY),'type of listY')

#Numpy has wide verity of mathematical functions to be reused 
# it is best lib for array operations because arrays are less memeory and fast.


#Lecture 2 
# Numpy Array VS Python List 
# Data type is same in array but mixture allowed in list list=[1,2,3,'hello',4,2,11,'Noor,]
#Numeric operations faster and wide range in numpy Array

#  to calculate execution time   timeit
import timeit

var1 = 900
var2 = 100

execution_time = timeit.timeit(
    'var1 * var2',
    globals=globals(),
    number=1000
)
print("Execution time:", execution_time)


# Array in numpy
# 1 Dimenssion array in NP
varList=[1,2,3,4]
varArr=NP.array(varList)
print(varArr,'1 D Array from list ====>')

# Input function in Python

# name = input("Enter your name: ")
# print("Hello", name)

#2D 3D and multidimennion Array 
Array2D=NP.array([[1,2,3,4]])
print(Array2D,Array2D.ndim,'Dimmession Array')

Array3D=NP.array([[[1,2,3,4]]])
print(Array3D,Array3D.ndim,'Dimmession Array')

ArrayND=NP.array([1,2,3,4],ndmin=10)
print(ArrayND,ArrayND.ndim,'Dimmession Array')


# Zero matric
arr_Zero=NP.zeros((3,3))
print(arr_Zero,'Zero matric cration 3,3')

# Ones matric
arr_Ones=NP.ones((3,3))
print(arr_Ones,'Ones matric cration 3,3')

# Diagonal or identity matric
arr_Diag=NP.eye(3,3)
print(arr_Diag,'Identity matric cration')

# Range matric-- create elements in a range
arr_Range=NP.arange(8)
print(arr_Range,'Range matric cration')

# Line Space in array kinda crate a gap in elements
arr_Space=NP.linspace(0,20,num=10)
print(arr_Space,'Space matric cration')

# Random Package and its functions for generating arrays with data
randFun=NP.random.rand(2)
print(randFun,'rand fun with 2 values single dimenssion array')


randFun2=NP.random.rand(2,4)
print(randFun2,'rand fun with 2 values single dimenssion array')
 












