from math import pi
import math
class math_operations:
    def __init__(self, *args):
        self.var = args if type(args) == list else list(args)
        


    
    def operation(self,operator):
        match operator:
            case 'lcm':
                return math.lcm(self.var[0],self.var[1])
            case 'circle':
                return (math.pi * float(self.var[0]) **2 )  if len(self.var)== 1 else "circle 연산자에서는 변수를 1개만 입력하시요"
            case 'factorial':
                return math.factorial(int(self.var[0])) if len(self.var)== 1 else " factorial 연산자에서는 변수를 1개만 입력하시요"
            case 'gcd':
                return math.gcd(self.var[0],self.var[1])
            
                


