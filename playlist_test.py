from ll import LinkedList, Node
from playlist import canciones



ll = LinkedList()
for i, cancion in enumerate(canciones):
    node = Node(data=i, song=cancion["song"], artist=cancion["artist"], album=cancion["album"])
    ll.insert_at_end(node)

#print(ll)

print(ll)
print(ll)