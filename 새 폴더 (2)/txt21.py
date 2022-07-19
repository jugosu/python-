n=int(input())
answer=0
while n>0:
    k=n%10
    answer=(answer*10)+k
    n//=10
print(answer)