class test:
    a = 5
    def __init__(self, real, imag, fake):
        self.r = real
        self.i = imag
        self.f = fake

    
x = test(3, 5, 15)
print(f"{x.r}")
print(x.i)
print(x.f)