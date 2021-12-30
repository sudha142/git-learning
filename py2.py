a=1
def f1():
    global a
    a=2
    print("local variable")
    print(a)
f1()
print("global variable")
print(a)