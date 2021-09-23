def binary_search(arr, low, high, x, i):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return i
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            i+=1
            return binary_search(arr, low, mid - 1, x, i)
            
 
        # Else the element can only be present in right subarray
        else:
            i+=1
            return binary_search(arr, mid + 1, high, x, i)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
t=int(input())
while t>0:
    t-=1
    y=int(input())
    
    arr = list(range(1,y+1))
    x = y
 
    # Function call
    i=1
    result = binary_search(arr, 1, len(arr)-1, x, i)
     
    if result != -1:
        print(str(result))
