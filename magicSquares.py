'''
Magic Squares is a special nxn square matrix where the sum of every row, every
 column and every diagonal is n(n**2 + 1)/2.
Algorithm : There are numbers from 1 to n**2
			1 is stored at position (n//2,n-1)	# starting point
			(i,j) ==> (i-1,j+1) 				# next postion
			if i = -1 ==> i = n-1				#
			if j = n ==> j = 0 
			if position is occupied, then i = i+1, j = j-2 
			if (-1,n) ==> (0,n-2)

'''

n = int(input('Please enter the size of the square : '))
if n <= 1:
	print('Please enter a higher number.')
	n = int(input('Enter the size : '))

# initialization
square = [[0 for i in range(n)] for j in range(n)]

#starting point
r = n//2
c = n-1
num = 1

#generation
while num <= n**2:
	if r == -1 and c == n: #last condition
		r,c = 0,n-2
	else:
		if c == n:			# columns goes out of bound
			c = 0
		if r < 0:			# row goes out of bound
			r = n-1
	if square[r][c]:			# if point is occupied
		r,c = r+1,c-2
		continue
	else:
		square[r][c] = num
		num += 1
	r,c = r-1,c+1

# printing the magic square
print('The magic square is : ')
for i in range(n):
	for j in range(n):
		print(square[i][j],end = ' ')
	print('\n')