import numpy as np
from numpy.linalg import eig
def valid(v):
	while True:
		if v.isdigit() and int(v)>0:
			return eval(v)
		else:
			v=input("enter right value")
def valid1(x):
	while True:
		try:
			return eval(x)
		except:
			x = input("correct value")
while True:
	r1=valid(input("enter row of mat1"))
	c1=valid(input("enter column of mat1"))
	if r1==c1:
		mat1=[[valid1(input(f"enter element  of mat1 posotion [{j}][{i}]  : ")) for i in range(c1)]for j in range(r1)]
		e,v = eig(np.array(mat1))
		print("eigen value ",e,"eigen vector",v)
		break
	else:
		print("matrix is not square not possible to find eigen value and eigen vector")