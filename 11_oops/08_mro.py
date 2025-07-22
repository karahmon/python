class A:
    label = "A : Base Class"

class B(A):
    label = "B : Masala Blend"

class C(A):
    label = "C : Herbal Blend"


class D(B,C):
    pass

cup = D()
print(cup.label) #prints first class provided in params
print(D.__mro__) # shows all inheritence


