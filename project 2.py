class calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"The value of the:{self.number}square is:{self.number**2}")
    def squareRoot(self):
         print(f"The value of the:{self.number}squareRoot is:{self.number**0.5}")
    def cube(self):
         print(f"The value of the:{self.number}cube is:{self.number**3}")
a=calculator(4)
a.square()
a.squareRoot()
a.cube()
