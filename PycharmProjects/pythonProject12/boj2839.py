
a=int(input())
count=0
while True:
    if(a%5==0):
        count+=a//5
        break
    a-=3
    count+=1
    if(a<0):
        count=-1
        break

print(count)



