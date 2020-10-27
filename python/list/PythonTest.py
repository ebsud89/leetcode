i = 'Hello world~ I love Python! I like pizza.'

newList = i.split()
print(newList)
# ['Hello', 'world~', 'I', 'love', 'Python!', 'I', 'like', 'pizza.']

newList = i.split('~')
print(newList)
# ['Hello world', ' I love Python! I like pizza.']

newList = i.split(maxsplit=2)
print(newList)
# ['Hello', 'world~', 'I love Python! I like pizza.']

newList = 'a,b,c,d,e'.split(',', maxsplit=2)
print(newList)
# ['a', 'b', 'c,d,e']

i = '''Hello world~
I love Python!
I like pizza.'''

newList = i.splitlines()
print(newList)
# ['Hello world~', 'I love Python!', 'I like pizza.']

newList = i.split('\n')
print(newList)
# ['Hello world~', 'I love Python!', 'I like pizza.']

newList = list("test")
print(newList)


def sum_coroutine():
    varr = 1
    total = f"test coroutine {varr}"
    while True:
        x = (yield total)  # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        total += x


co = sum_coroutine()
print(next(co))  # 0: 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력