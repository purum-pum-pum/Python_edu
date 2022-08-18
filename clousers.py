def func_1():
    st = 'Hello world!'
    def func_2():
        return st
    return func_2

f = func_1()
print(f())


