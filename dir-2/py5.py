def outer(who):
    print("hei",who)
    def inner():
        print(f"hello,{who}")
    inner()
outer("world")