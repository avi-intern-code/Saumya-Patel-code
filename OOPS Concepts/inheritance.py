class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(): #single level inheritance
    def __init__(self):
        print("in B init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(B): #multilevel inheritance
    def __init__(self):
        print("in C init")

    def feature5(self):
        print("Feature 5 working")

class D(A,B): #multilevel inheritance
    def __init__(self):
        super().__init__()
        print("in D init")

    def feature6(self):
        print("Feature 6 working")

    def feat(self):
        super().feature2() #super to call other methods

a1 = A()
a1.feature2()

b1 = B()
# b1.feature1()

c1 = C()
c1.feature4()

d1 = D()
d1.feature1() # leftest element
d1.feat()