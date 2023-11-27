class D:
    pass

class A:

    def class_a_method(self):
        print('I\'m Just a class A Mehod')

    def hello(self):
        print('Hello from class A')


class B(D):
    def class_b_method(self):
        print('I\'m Just a class B Mehod')

    def hello(self):
        print('Hello from class B')

class C(B,A):
    pass


instance_c=C()
# print(instance_c.class_a_method())
# print(instance_c.class_b_method())
print(instance_c.hello())
# print(help(C))
# print(C.mro())
# print(C.__mro__)