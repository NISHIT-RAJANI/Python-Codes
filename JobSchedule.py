Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def jobschedule(arr,t):
    for i in range(len(arr)):#sorting 
        for j in range(len(arr)-1-i):
            if(arr[j][2])<(arr[j+1][2]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    result=[False]*t
    job=['0']*t
    for i in range(len(arr)):
        for j in range((arr[i][1]-1),-1,-1):
            if(result[j] is False):
                result[j]=True
                job[j]=arr[j][0]
                break
    print(job)
            


arr=[['a',2,100],['b',1,10],['c',2,30],['d',2,25],['e',3,15]]
jobschedule(arr,3)