import math
class PowerofTwo:
    def __init__(self):
        self.isValid = False
    def isPowerofTwo1(self, n):

        if (n == 1):
            self.isValid = True
        elif (n <= 0):
            self.isValid = False
        elif(n % 2 != 0):
            self.isValid = False
        else:
            for i in range(1, math.ceil(n ** 2) + 1):
                if (n == 2 ** i):
                    self.isValid = True
            
        return self.isValid
    
    def isPowerofTwo2(self, n):
        if(n <= 0):
            return False
        else:
            return n & (n-1) == 0    
#create an instance of the class
number = PowerofTwo()

print(number.isPowerofTwo2(16))