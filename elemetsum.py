ans = 0
def validate(x):
	while True:
		if x.isdigit() and int(x)>0:
			return eval(x)
		else:
			x=input("enter the correct value : ")
def valid1(y):
	while True:
		try:
			return eval(y)
		except:
			y = input("correct value")
	
r1=validate(input("enter row of mat1 : "))
c1=validate(input("enter coloumn of mat1 : "))
mat1=[[valid1(input(f"enter element  of mat1 [{j}][{i}]  : ")) for i in range(c1)]for j in range(r1)]
for i in range(r1):
	for j in range(c1):
		ans+=mat1[i][j]
print(mat1)
print(ans)