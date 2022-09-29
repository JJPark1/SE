n = int(input())
l=[]
for i in range(n):
    l.append(input())

set_word = list(set(l))


set_word.sort(key=lambda x : (len(x),x))

print("\n".join(set_word))

