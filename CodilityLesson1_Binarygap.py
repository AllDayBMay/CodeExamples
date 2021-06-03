"""
Submitted on 06/03/2021, this is my answer to a Codility training task, in which
my aim was to write a function that would return the size
of the largest binary gap (a string of 0's with a 1 on either side)
More info here: https://app.codility.com/demo/results/training6H53UQ-85Z/
"""

def solution(N):
    #First, find the binary representation of the decimal number
    binaryRepresentation = []
    while (N > 0):
        div = N % 2
        binaryRepresentation.append(div)
        N=N//2
    i = 0
    #remove front zeros, which would end up being end zeros after reversal, which are not flanked by a 1 on the left side
    while (binaryRepresentation[i] == 0 and i < len(binaryRepresentation)):
        del binaryRepresentation[0]
    binaryRepresentation.reverse()
    """
    print('Binary Representation:')
    print(binaryRepresentation)
    """
    gap_lengths = []
    max_gap_length = 0
    current_gap_length = 0
    i = 0
    #Propertly increment max_gap_length and gap_length
    while (i < len(binaryRepresentation)):
        if (binaryRepresentation[i] == 0 and current_gap_length < max_gap_length):
            current_gap_length = current_gap_length + 1
            i = i + 1
            """
            print('a, max, current, i:')
            print(max_gap_length)
            print(current_gap_length)
            print(i)
            """
        elif (binaryRepresentation[i] == 0):
            max_gap_length = current_gap_length + 1
            current_gap_length = current_gap_length + 1
            i = i + 1
            """
            print('b, max, current, i:')
            print(max_gap_length)
            print(current_gap_length)
            print(i)
            """
        else:
            current_gap_length = 0
            i = i + 1
            """
            print('c, max, current, i:')
            print(max_gap_length)
            print(current_gap_length)
            print(i)
            """
    """        
    print('max gap length:')
    print(max_gap_length)
    """
    return max_gap_length
   