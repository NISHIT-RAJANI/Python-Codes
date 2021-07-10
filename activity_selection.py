Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def activityselection(s,f):
    activity=[]
    index=[i for i in range(len(s))]
    index.sort(key=lambda i:f[i])
    activity+=[index[0]]
    finishtime=f[index[0]]
    for k in range(len(index)):
        ind=index[k]
        if(s[ind]>=finishtime):
            activity+=[ind]
            finishtime=f[ind]
    return activity
        





#a=[0,1,2,3,4,5,6]
s=[1,4,7,3,2,8,9]
f=[4,6,8,5,3,10,11]
activity=activityselection(s,f)
print(activity)