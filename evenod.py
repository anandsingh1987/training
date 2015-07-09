def evenod():
	a=input()
	if (a%2):
		print "number %d is odd"%(a)
	else: 
		print "number %d is even"%(a)

# it is for modulos of two numbers
def Mymod(num1 ,num2):
	return num1-(num1/num2)*num2


evenod()
print Mymod(7,9)
