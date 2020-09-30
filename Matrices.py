import numpy as np
import math, time


def translation2D(angle):
    theta = (angle/180)*(np.pi)
    e11 = np.cos(theta)
    e12 = -np.sin(theta)
    e21 = np.sin(theta)
    e22 = np.cos(theta)
    temp = [[e11,e12],[e21,e22]]
    return np.array(temp)

def translation3D(angle):
    theta = (angle/180)*(np.pi)
    e11 = np.cos(theta)
    e12 = -np.sin(theta)
    e13 = 0
    e21 = np.sin(theta)
    e22 = np.cos(theta)
    e23 = 0
    e31,e32,e33 = 0,0,1
    temp = [[e11,e12,e13],[e21,e22,e23],[e31,e32,e33]]
    return np.array(temp)



def reflection2D(angle):
    theta = (angle/180)*(np.pi)
    e11 = np.cos(theta)
    e12 = np.sin(theta)
    e21 = np.sin(theta)
    e22 = -np.cos(theta)
    temp = [[e11,e12],[e21,e22]]
    return np.array(temp)

def reflection3D(angle):
    theta = (angle/180)*(np.pi)
    e11 = np.cos(theta)
    e12 = np.sin(theta)
    e13 = 0
    e21 = np.sin(theta)
    e22 = -np.cos(theta)
    e23 = 0
    e31 = 0
    e32 = 0
    e33 = 1
    temp = [[e11,e12,e13],[e21,e22,e23],[e31,e32,e33]]
    return np.array(temp)


def HouseHolder(u):
    I = np.identity(len(u))
    temp = np.dot(u, u.transpose())
    ans = I-temp
    return ans


def is_orthogonal(A):
    t1 = A.transpose()
    t2 = np.linalg.inv(A)
    return (t1 == t2)[0][0]


def Hadamard(n):
    
    if n%4 == 0:
        H = np.ones((n,n))
        i1 = 1
        while i1 < n:
            for i2 in range(i1):
                for i3 in range(i1):
                    H[i2+i1][i3]    = H[i2][i3]
                    H[i2][i3+i1]    = H[i2][i3]
                    H[i2+i1][i3+i1] = -1
                    print(i3)
            i1 += i1

        return H
    elif n == 1:
            return np.array([1])
    elif n == 2:
            return np.array([[1,1],[1,-1]])
    else:
        return "No Hadamard Matrix, Only when 'N/4' is whole number"



def Haar(n):
    if n == 4:
        t = 1/(np.sqrt(4))
        s = 1/(np.sqrt(2))
        temp = [[t,t,s,0],[t,t,-s,0],[t,-t,0,s],[t,-t,0,-s]]
        return np.array(temp)
    elif n ==8:
        p = 1/(np.sqrt(8))
        q = 1/(np.sqrt(4))
        r = 1/(np.sqrt(2))
        temp = [[p,p,q,0,r,0,0,0],
                [p,p,q,0,-r,0,0,0],
                [p,p,-q,0,0,r,0,0],
                [p,p,-q,0,0,-r,0,0],
                [p,-p,0,q,0,0,r,0],
                [p,-p,0,q,0,0,-r,0],
                [p,-p,0,-q,0,0,0,r],
                [p,-p,0,-q,0,0,0,-r]]
        return np.array(temp)

a = Haar(4)
# print(a)
# print(is_orthogonal(a))

# ev = np.linalg.eigvals(a) 

# print(ev)

dd = np.linalg.svd(a)
print(dd)



