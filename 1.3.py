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
        while ( (ptr.nxt) != (None) ) :      # Line 11 main ptr  starting node ko point ker raha phir line
            ptr = ptr.nxt                    # 12 main ham node kai next ko access ker rahay aur check ker
                                             #  rahay None kahan ai ga Line 13 main ptr ko aglay node kai next
                                             # per ker rahay send if nhi milta None pehlai aur ya loop chalta 
                                             # jab tak nhi milta nxt main 
        ptr.nxt = Node(i,None)
        
L=SLList()
L.Addfirst(5)
L.Addfirst(10)
L.Addlast(20)
