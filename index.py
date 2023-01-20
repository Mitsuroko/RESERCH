class MyClass:
    def __init__(self):
        self.name = "tanaka"
        self._name = "yamada"
        self.__name = "suzuki"

    def hello(self): print('hello')
    def _hello(self): print('hello!')
    def __hello(self): print('hello!!')

a = MyClass()

print(a.name)           # 参照できる
print(a._name)          # 参照できるが慣習的に参照しない
# print(a.__name)       # 参照できない(AttributeError例外)
print(a._MyClass__name) # 名前が変わっただけなので、この名前にしてあげれば参照できる

a.hello()               # 参照できる
a._hello()              # 参照できるが慣習的に参照しない
# a.__hello()           # 参照できない(AttributeError例外)
a._MyClass__hello()     # 名前が変わっただけなので、この名前にしてあげれば参照できる