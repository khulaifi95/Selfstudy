class Base(object):
    def __init__(self):
        print('enter Base')
        print('leave Base')


class A(Base):
    def __init__(self):
        print('enter A')
        super(A, self).__init__()
        print('leave A')


class B(Base):
    def __init__(self):
        print('enter B')
        super(B, self).__init__()
        print('leave B')


class C(A, B):
    def __init__(self):
        print('enter C')
        super(C, self).__init__()
        print('leave C')


C()

print(C.mro())

# Equal to below without super()
# Multiple base class call


class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")


class A(Base):
    def __init__(self):
        print("enter A")
        Base().__init__()
        print("leave A")


class B(Base):
    def __init__(self):
        print("enter B")
        Base().__init__()
        print("leave B")


class C(A, B):
    def __init__(self):
        print("enter C")
        A().__init__()
        B().__init__()
        print("leave C")


# C()
