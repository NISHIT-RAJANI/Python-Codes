Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def binarysearch(arr,l,r,key):
    
    if(l<=r):#base case
        mid=int((l+r)/2)
        
        if(arr[mid]==key):
            return mid
        elif(arr[mid]<key):
            return binarysearch(arr,mid+1, r, key)
        else:
            return binarysearch(arr,l, mid-1, key)
    else:
        return -1
arr=[2,4,6,7,9,12,14]
key=9
status=binarysearch(arr, 0, len(arr)-1, key)
if(status==-1):
    print("Element not found")
else:
    print("Element is found at index",status)