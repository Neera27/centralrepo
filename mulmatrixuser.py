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
	r2=valid(input("enter row of mat2"))
	c2=valid(input("enter column of mat2"))
	if c1==r2:
		mat1=[[valid1(input(f"enter element  of mat1 posotion {j}{i}  : ")) for i in range(c1)]for j in range(r1)]
		mat2=[[valid1(input(f"enter elementof  mat2 posotion {j}{i}  : ")) for i in range(c2)]for j in range(r2)]
		ans = [[0 for i in range(c2)]for j in range(r1)]
		for i in range(r1):
			for j in range(c2):
				for k in range(r2):
					ans[i][j] += mat1[i][k] * mat2[k][j]
		print(ans)
		break
	else:
		print("mat mul not possible")