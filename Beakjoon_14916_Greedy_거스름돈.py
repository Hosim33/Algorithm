#백준 14916

n = int(input())
coin = n % 5
if(n==1 or n==3):
    result = -1;
elif(coin%2==0):
    result=n//5+coin//2
else:
    result=((n//5)-1)+((coin+5)//2)
print(result)
