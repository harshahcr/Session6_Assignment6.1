# function so that the columns of the output matrix are powers of the input vector
import numpy as np
#input array; N = integer
x = np.array([1, 2, 3, 5, 8])
N = 7
vanf= np.vander(x, N, increasing= False)
print(vanf)
#If True, the powers increase from left to right
N = 5
vant= np.vander(x, N, increasing= True)
print(vant)
