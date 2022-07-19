T= int(input())
for i in range(1, T+1):
    a=list(map(int,input().split()))
    ssq=sum(a)/len(a)
    ssq=round(ssq)
    print('#{}  {}'.format(i,ssq))
    