Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def matrix(d,n):
  m=[[0 for i in range(n)]for j range(n)]
  for i in range(1,n):
    m [i][j]=0
    for D in range(1,n-d):
      for i in range(1,n-d)
      j=i+d
      for k in range(i,j):
        q=m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]
        if(q<m[i][j]:
           m[i][j]:
           m[i][j]=q
           return m[1][n-1]
  d=[5,4,6,2,7]   
  size=len(d)  
  m=matrix
