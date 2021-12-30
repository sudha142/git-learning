def function1():
    print("hello from outer function")
    def function2():
        print("hello from inner function")
    function2()