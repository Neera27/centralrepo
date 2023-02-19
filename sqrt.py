# problem is to find squeroot of any number
while True:
    a=input("Enter any no")
    try:
        print(f"Squreroot of numer {a} is : {eval(a)**0.5}") # "**" is power operator for squreroot poer is 1/2 or 0.5 
        break
    except:
        print("wrong input enter numeric value")