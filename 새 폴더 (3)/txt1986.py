from re import I


x=int(input())
for c in range(1,x+1):
    z=int(input())

    sum=1
    for i in range(2, z+1):
        if i%2 == 0:
            sum-=i
        else :
            sum+=i

    print('#{} {}'.format(c,sum))