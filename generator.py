# 生成器函数


def f():
    print('ok1')
    yield  # 1
    print('ok2')
    num = yield  # 2
    print(num)
    print('ok3')
    yield  # 3


gen = f()

gen.__next__()  # 1
gen.__next__()  # 2

gen.send(5)  # 3
gen.__next__()

