"""
Submitted on 06/03/2021, this is my answer to a Codility training task, in which
my aim was to write a function that would rotate each value in an array A
to K spaces to the right.
More info here: https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
"""  
    

def solution(A, K):
    #Start with a matrix of zeros
    B = [0]*len(A)
    i = 0
    #If K and the length of A is equal, just return A.
    if (K==len(A)+1):
        return A
        #Otherwise, rotate:
    else:
        if(K > len(A)):
            K = len(A)%K
        while (i < len(A)-K):
            B[i+K]=(A[i])
            i = i + 1
            print('A:')
            print(A)
            print('B:')
            print(B)
            print('i')
        i=0
        while (i < len(A)-K+1):
            B[i] = A[i+K-1]
            i = i + 1
            print('A:')
            print(A)
            print('B:')
            print(B)
            print('i')
            print(i)
        return(B)
