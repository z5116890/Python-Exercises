'''
Define a recursive function that, takes in an index n will calculate the n-th number in the fibonacci sequence.
The fibonacci sequence is defined as 
f(x) = 
	| x == 0     = 0
	| x == 1     = 1
	| otherwise  = f(x - 1) + f(x - 2)
The index is to be read from the standard input and 
the fibonacci number at that index is to be printed
to the standard output. You may assume that your
program will be tested with valid inputs only.
'''

#Initialising a dictionary with a fibonacci series of 4 elements
fib_dict = {
	0: 0,
	1: 1,
	2: 1,
	3: 2
}

# Define this recursive function to return the expected output
# Do not print it from this function
def fib_sequence(num):
	# to be completed
	if num not in fib_dict: # 4
		fib_dict[num] = fib_sequence(num - 1) + fib_sequence(num - 2)
	else:
		pass 

	return fib_dict[num]





if __name__ == '__main__':
	#write code to accept user input, call the function and print the result
	print(fib_sequence(10))


	num = int(input("enter number "))
	try:
		val = int(num)
	except ValueError:
		print("That's not an int!")

	fib = fib_sequence(num)
	print(fib)



