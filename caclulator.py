class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def addition(self):
        return (self.a + self.b)

    def subtraction(self):
        return (self.a - self.b)

    def multiplication(self):
        return (self.a * self.b)

    def floor_division(self):
        return (self.a / self.b)
    
    def float_division(self):
        return (self.a // self.b)
    
    def power(self):
        return (self.a ** self.b)
    
    def mod_division(self):
        return (self.a % self.b)
    
sel=1
while sel!=8:
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Floor Division\n5.Float Division\n6.Power\n7.Mod Division\n8.Exit")
    sel=int(input("Enter your selection: "))
    a=int(input("Enter number 1: "))
    b=int(input("Enter number 2: "))
    obj=calculator(a,b)
    if sel==1:
        print("Addition is:",obj.addition())
    elif sel==2:
        print("Subtraction is:",obj.subtraction())
    elif sel==3:
        print("Multiplication is:",obj.multiplication())
    elif sel==4:
        print("Floor Division is:",obj.floor_division())
    elif sel==5:
        print("Float Division is:",obj.float_division())
    elif sel==6:
        print("Power is:",obj.power())
    elif sel==7:
        print("Mod Division is:",obj.mod_division())
    else:
        print("Please enter a valid choice")