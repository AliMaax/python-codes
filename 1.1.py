class Node:
    def __init__ (self,i,n):
        self.item=i
        self.nxt=n
class SLList:
    def __init__(self):
        self.sentinel=Node(63,None)


L=SLList()