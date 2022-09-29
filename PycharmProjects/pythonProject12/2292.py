"""a=int(input())
count =1
front=2
back=7
tmp=0
while True:
    if(a==1):
        tmp=count
        break
    count+=1
    if a>= front and a<=back:
        tmp=count
        break
    front=back+1
    back+=count*6


print(tmp)

"""

a= int(input())
count=1
sum=1
while True:
    if(a==1):
        print(count)
        break
    sum+=count*6
    if(a<=sum):
        print(count+1)
        break