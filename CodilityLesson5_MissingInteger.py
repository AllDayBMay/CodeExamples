"""
Submitted on 06/04/2021, this is my answer to a Codility training task, in which
my aim was to write a function that would identify a missing element in an array in which
the elements (1,2,....N+1) were contained in an array of size N. This was graded on efficiency
and has time efficiency O(n).
More info here: https://app.codility.com/demo/results/training4UKCCE-7PY/
"""  
    
def solution(A):
    count = [0] * (len(A)+1)
    i = 0
    while (i < len(A)):
        count[A[i]-1]=1
        i = i + 1
    i = 0
    while (count[i] == 1):
        i = i + 1
    return i+1