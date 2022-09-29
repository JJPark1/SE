
def func2(str):
    list_str=list(str)
    list_str[0]='h'
    str="".join(list_str)
    return str

def func1():
    str=input("문자열을 입력하시오: ")
    print("변경된 문자열:"+func2(str))

def func4(n):
    list_n=n.split()
    x=int(list_n[0])
    y=int(list_n[1])
    x=x*x*x
    y=y*y*y
    if(x>y):
        a=x-y
    else:
        a=y-x
    return a
def func3():
    n=input("정수 두 개를 입력하시오: ")
    print("두 정수의 세제곱차: %d"% func4(n))
func1()
func3()
