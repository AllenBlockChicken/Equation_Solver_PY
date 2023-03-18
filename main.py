# -*- coding: UTF-8 -*-
#! python3

class OnceEquation():
    
    def __init__(self,k:int,b:int):
        self.k = k 
        self.b = b 
        
    
    def deal(self):
        value =self.b/self.k*-1
        if value%1 == 0:
            return str(int((value)))
        else:
            return("-"+str(int(self.b))+"/"+str(int(self.k)))

class TwiceEquation():
    
    def __init__(self,a:int,b:int,c:int):
        self.a = a
        self.b = b
        self.c = c


    def ifInt(self,x):
        if x%1 == 0:
            return(1)
        else:
            return(0)
    
    def deal(self):
        b_twice = self.b**2
        a_c_four = 4 * self.a * self.c
        delta = b_twice - a_c_four
        if delta < 0:
            print ("此方程无解")
            return(0)
            
        elif delta == 0:
            b_ = -1 * self.b
            a_two = 2 * self.a 
            value = b_/a_two
            if self.ifInt(value):
                X = [value,value]
                return(X)
                
            else:
                X = [str(b_)+"/"+str(a_two),str(b_)+"/"+str(a_two)]
                return(X)
            
