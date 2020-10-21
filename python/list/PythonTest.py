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