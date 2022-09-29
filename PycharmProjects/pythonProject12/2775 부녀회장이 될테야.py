

t=int(input())
while t>0:
    k=int(input())
    n=int(input())
    list1 =[]
    # list1 = [ i for in range(1,n+1)]
    for i in range(1,n+1):
        list1.append(i)

    for j in range(k):
        for x in range(1,n):
            list1[x]+=list1[x-1]
    print(list1[-1])

    t-=1






