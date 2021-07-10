Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def knapsack_DP(W,weight,profit,n):
    if n==0 or W==0:  
        return 0
    if(weight[n-1]>W):
        return knapsack_DP(W, weight, profit, n-1)
    else:
        return max(profit[n-1]+knapsack_DP(W-weight[n-1], weight, profit, n-1),knapsack_DP(W, weight, profit, n-1))
        
    
W=50
weight=[10,20,40]
profit=[60,100,120]
n=len(profit)
print("max :",knapsack_DP(W,weight,profit,n))