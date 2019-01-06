import numpy as np

class Cell():
    def __init__(self,val,grad):
        self.val=val
        self.grad=grad

class Gate():
    def forward(self):
        pass
    
    def backprop(self):
        pass

class Circuit():
    def forward(self):
        pass
    
    def backprop(self):
        pass

    def adjust(sefl):
        pass

class AddGate(Gate):
    def forward(self,c0,c1):
        self.c0=c0
        self.c1=c1
        self.out=Cell(self.c0.val+self.c1.val,0.0)
        return self.out
    
    def backprop(self):
        self.c0.grad+=1.0*self.out.grad
        self.c1.grad+=1.0*self.out.grad

class ProdGate(Gate):
    def forward(self,c0,c1):
        self.c0=c0
        self.c1=c1
        self.out=Cell(self.c0.val*self.c1.val,0.0)
        return self.out
    
    def backprop(self):
        self.c0.grad+=self.c1.val*self.out.grad
        self.c1.grad+=self.c0.val*self.out.grad

class LinearCircuit(Circuit):
    def __init__(self):
        