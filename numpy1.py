import numpy as np
a=np.array([1,2,3,4,5,6])
print(type(a),a)
a=np.array([
[1,2,3],[4,5,6],[7,8,9]])
print(a)
a=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]]])
print(a[1][2][2])

#L=list(map(int,input("enter value").split()))
a=np.array([2.464,4,5,6.5],dtype='S')
print(a[0],a.dtype)
