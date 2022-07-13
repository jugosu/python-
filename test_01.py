
# num = int(input())
# if num % 2 == 0: 
#   print('짝수입니다.')

 #else :
  # print('홀수입니다.')

#dust = int(input())

#f dust >150:
    #if dust>300:
        #print('미세먼지 농도가 높습니다.')
    #print('매우 나쁨')
    
#elif dust > 80:
    #print('나쁨')
#elif dust > 30:
 #   print('보통')
#else :
 #   if dust < 0:
  #      print('음수입니다.')
   # else :
    #    print('좋음')
#n=0
#r=0
#user_input =int(input())
#while n<= user_input:
 #   print(f'n:{n}, result:{r}')
  #  r+=n
   # n+=1

#n=0
#r=0
#user_input =int(input())
#while n< user_input:
 #   print(f'n:{n}, result:{r}')
 #   n+=1
 #   r+=n
#n=int(input())
#user_input=0
#if user_input == n%2 and n %3 == 0:
#    print('참') 
#else :
#    print('거짓')

#word=input()
#a=0
#for b in word:
#    a+=1
#print(a)

#word=input()
#a=0
#for b in range(len(word)):
 #   a+=1
#print(a)

#a=0
#b=0
#num= int(input())
#while a<num:
 #   a+=1
  #  b+=a
#print(b)

#a=0
#num= int(input())
#for b in range(1,num+1):
#    a+=b
#print(a)

#a=0
#b=1
#num= int(input())
#while a<num:
#    a+=1
#    b*=a
#print(b)

#=1
#num= int(input())
#for b in range(1,num+1):
 #   a*=b
#print(a)

#a=[3,10,20]
#b=(a[0]+a[1]+a[2])/3
#print(int (b))

#numbers = [0, 20, 100]
#max = numbers[0]
#for i in numbers:
#    if max < i:
#       max = i

#numbers.remove(max)
#max = numbers[0]
#for i in numbers:
#    if max < i:
#       max = i
#print(max)
#numbers=[3,10,20]
#sum =0
#for i in range(3):
#    sum+=numbers[i]
#print(int(sum/3))
#import math
#n= int (input())
#print(n,'',math.pow(n,3))
#def cube(n):
#    return n**3
#print(cube(12))
#a=int(input())
#b=int(input())
#def w(a,b):
#    return a*b
#def r(a,b):
#    return (a+b)*2
#def rectangle(a,b):
#    return (w(a,b),r(a,b))
#print(rectangle(a,b))
#a=20
#b=30
#def rectangle(a,b):
#    area= a*b
#    perimeter = 2*(a+b)
#    return area, perimeter
#print(rectangle(20,30))
#students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
#x=0
#for i in students:
#    if '이영희'==i:
#            x+=1
#print(x)

#numbers = [7,17,10,5,4,3,17,5,2,5]
#x=0
#for i in numbers:
#    if 5 == i:
#        x+=1
#print(x)
#for i in range(2,10):
#    print(i,'단')
#    for y in range(1,10):
#        print(i,'X',y,'=',i*y)

#word = 'apple'
#result = ''
#for char in 'apple':
#    if char != 'a':
#        #print(char)
#        result = result + char
#print(result)
        
#word = 'apple'
#result = ''
#for char in 'apple':
#    if char != 'a':
#        #print(char)
#        result = char + result
       
#print(word[::-1])
#print(''.join(reversed(word)))
#print(result)

word = 'apple'

for i in range(len(word)):
    print(word[len(word)-i-1], end='')