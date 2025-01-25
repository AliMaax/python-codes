class Node:
    def __init__ (self,i,n):
        self.item=i
        self.nxt=n
class SLList:
    def __init__(self):
        self.sentinel=Node(63,None)
    def Addfirst(self,i):
        self.sentinel.nxt = Node(i,self.sentinel.nxt)    
    def Addlast(self,i):
        ptr = self.sentinel
        while ( (ptr.nxt) != (None) ) :  
            ptr = ptr.nxt                    
        ptr.nxt = Node(i,None)
        
L=SLList()
L.Addfirst(5)
L.Addfirst(10)
L.Addlast(20)