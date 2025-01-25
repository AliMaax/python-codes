from sentinellinkedlist import *

L = SLList()
L.Addfirst(5)
L.Addfirst(10)
L.Addlast(20)
print(L.sentinel.nxt.item)
assert(L.sentinel.nxt.item == 10)