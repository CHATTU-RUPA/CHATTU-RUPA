import numpy as np
A=np.array(input("enter the first array:"))
B=np.array(input("enter the second array:"))
C=A+B
print"addition of matrix:",C;
D=A-B
print"subtraction of matrix:",D;
E=A.dot(B)
print"multiplication of matrix:",E;
Y=A/B
print"division of matrix:",Y;
F=(A.transpose())
print"transpose of matrix:",F;
Y=np.linalg.det(A)
print"determinant of matrix:",Y
V=np.linalg.eig(A)
print"eigen values of matrix:",V
W=np.square(B)
print"square of the matrix:",W
Q=np.max(B)
print"maximum of the matrix:",Q
I=np.min(A)
print"minimum of the matrix:",I
T=np.zeros((2,2))
print"zero matrix:",T
Z=np.ones((1,2))
print"ones matrix:",Z
J=np.eye(3)
print"identity matrix:",J








