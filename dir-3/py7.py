def function1():
    x=2
    def function2(a):
        x=6
        print("This is the inner function print statement:",a+x)
    print("before calling the second function x value will execute from the first function:",x)
    function2(3)
function1()