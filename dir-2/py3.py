a=1
def f1():
    b=2
    c=3
    def f2():
        d=4
        print("global value of 'a' inside nested function:",a)
        print("value from the above function 'b':",b)
        print(" local value of the nested function:",d)
        nonlocal c
        c=20
    print("before calling f2 function:",c)
    f2()
    print("non local updated value",c)
    print(b)
f1()
print(a)