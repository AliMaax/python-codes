class Node:
    def __init__ (self,i,n):
        self.item=i
        self.nxt=n
class SLList:
    def __init__(self):
        self.sentinel=Node(63,None)
        self.size = 0
    def Addfirst(self,i):
        self.sentinel.nxt = Node(i,self.sentinel.nxt)   
        self.size += 1  
    def Addlast(self,i):
        ptr = self.sentinel
        while ( (ptr.nxt) != (None) ) :   
            ptr = ptr.nxt                  
        ptr.nxt = Node(i,None)
        self.size += 1
    def getsize(self):
        return self.size      
L=SLList()
L.Addfirst(5)
L.Addfirst(10)
L.Addlast(20)
print(L.getsize())