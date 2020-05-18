MAX = 100;   
def luDecomposition(mat, n): 
	lower=[[0,0,0],[0,0,0],[0,0,0]]
	upper=[[1,1,1],[1,1,1],[1,1,1]]
	for i in range(n):  
		for k in range(i, n):  
			sum = 0; 
			for j in range(i): 
				sum += (lower[i][j] * upper[j][k])
		upper[i][k] = mat[i][k] - sum 
		for k in range(i, n): 
			if (i == k): 
				lower[i][i] = 1
			else: 
				sum = 0 
			for j in range(i): 
				sum += (lower[k][j] * upper[j][i]) 
		lower[k][i] = int((mat[k][i] - sum) / upper[i][i]) 
	print("Lower Triangular") 
	for i in range(n): 
		print(lower[i])
		print('\n')
	print("Upper Triangular")  
	for i in range(n): 
		print(upper[i]) 
		print('\n')
mat=eval(input('Enter matrice')) 
  
luDecomposition(mat, 3)

