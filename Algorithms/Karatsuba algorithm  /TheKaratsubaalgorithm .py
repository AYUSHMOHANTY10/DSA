# Implementation of Karatsuba algorithm 
# Using Divide and Conquer Approach

# A Function That Equals The Length Of The Two Strings
def L_Equal(s1, s2):
	l1 = len(s1)
	l2 = len(s2)
	if l1 < l2:
	    s1=s1.zfill(l2)
	    return l2
	elif l1 > l2:
	    s2=s2.zfill(l1)
	return l1

# The Main Multiplication Function
def Mult(x, y):

	# Equaling The Length Of The Numbers
	n = max(len(x), len(y))
	x = x.zfill(n)
	y = y.zfill(n)

	# Base Cases
	if n == 0: return 0
	if n == 1: return int(x[0])*int(y[0])

    # First & Second Half Of String
	fh = n//2 
	sh = n - fh 
	# Halves Of The First String 
	xs = x[:fh]
	xe = x[fh:]
	# Halves Of The Second String  
	ys = y[:fh]
	ye = y[fh:]

	# Recursively Calculating The Three Products Of Inputs Of Size {n/2}
	p = Mult(xs, ys)
	q = Mult(xe, ye)
	r = Mult(str(int(xs, 2) + int(xe, 2)), str(int(ys, 2) + int(ye, 2)))

	# Combining The Three Products To Get The Final Result.
	return p*(1<<(2*sh)) + (r - p - q)*(1<<sh) + q

a=(bin(int(input("Enter the 1st number: ")))).replace("0b","")
b=(bin(int(input("Enter the 2nd number: ")))).replace("0b","")
print("\nResult:")
print(Mult(a,b))
