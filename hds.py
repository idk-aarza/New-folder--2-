num=[1,2,3,4,5]
num2=[1,2,3,6,7]
a=map(lambda x,y:x+y, num,num2 )
print(list(a))
num1=[2,4,6,8]
def cube(n):
   return n**3
cubic=list(map(cube, num1))
print(cubic)