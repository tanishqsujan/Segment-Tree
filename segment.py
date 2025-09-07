from math import ceil, log2;

#Utility function to get the middle index from the corner indexes
def getmiddle(s, e):
    return s + (e - s) // 2

"""A recursive function to get the sum of values in the
given range of the array. The following are the parameters for this funtion.

st - Pointer to the segment tree
si - index of the current node in the segment tree
Initially 0 is passed as root is always at index 0
ss and se - Starting and Ending indexes of the segment represented by the current node, i.e, st[si]
qs and qe - Starting and Ending indexed of the query range"""

def getsumutil(st, ss, se, qs, qe, si):
    
    #If the segment of this node is a part of the given range, then return the sum of the segment
    if (qs <= ss and qe >= se):
        return st[si]
    
    #If segment of this node is outside the given range
    if (se < qs or ss > qe):
        return 0
    
    #If a part of this segment overlaps with the given range
    mid = getmiddle(ss, se)
    
    return (getsumutil(st, ss, mid, qs, qe, 2 * si + 1) + getsumutil(st, mid + 1, se, qs, qe, 2 * si + 2))

""" A recursive function to update the nodes
which have the given index in their range.
The following are parameters st, si, ss and se
are same as getSumUtil()
i --> index of the element to be updated.
	This index is in the input array.
diff --> Value to be added to all nodes
which have i in range """

def updatevalueutil(st, ss, se, i, diff, si):
    
    #Base case: if the input index lies outside the range of this segment
    if (i < ss or i >se):
        return
    
    st[si] = st[si] + diff
    
    if (se != ss):
        
        mid = getmiddle(ss, se)
        updatevalueutil(st, ss, mid, i, diff, 2 * si + 1)
        updatevalueutil(st, mid + 1, se, i, diff, 2 * si + 2)
        
def updatevalue(arr, st, n, i, new_val):
    
    #Check for erroneous input index
    if (i < 0 or i > n - 1):
        print("Invalid Input", end=" ")
        return
    
    #Get the difference between new value and old value
    diff = new_val - arr[i]
    
    #Update the value in array
    arr[i] = new_val
    
    #Update the values of nodes in segment tree
    updatevalueutil(st, 0, n - 1, i, diff, 0)
    
def getsum(st, n, qs, qe):
    
    #Check for erroneous values
    if (qs < 0 or qe > n - 1 or qs > qe):
        print("Invalid Input", end=" ")
        return -1
    
    return getsumutil(st, 0, n - 1, qs, qe, 0)

def constructstutil(arr, st, se, si, ss):
    
    #If there is one element in array, store it in curent node of segment tree and return
    if (ss == se):
        st[si] = arr[ss]
        return arr[ss]
    