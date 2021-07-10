Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def makingcoinchange(coin,amt):
    table = [0 for i in range(amt+1)]
    table[0]=1
    for i in range(len(coin)):
        for j in range(coin[i],amt+1):
            table[j]+=table[j-coin[i]]

    return table[amt]
coin=[2,3,5,10]
amt=15
print("There are possible combinations: ",makingcoinchange(coin, amt))