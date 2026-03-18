from typing import Any, Optional, Iterator


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = None
        self.prev: Optional["Node"] = None
        self.playlist = {"song":'', 
                         "artist":'',
                         "album": ''}

    def __repr__(self) -> str:
        return f'(DATA: {self.data} | NEXT: {self.next})'  # TODO: En el futuro arreglar repr para mostrar solo la data, error cuando next es None
    

class LinkedList:
    def __init__(self) -> None:
        self.start: Optional[Node] = None

    def __repr__(self) -> str:
        nodes = ['START']
        for node in self:
            nodes.append(node.data)
        nodes.append('NIL')
        return '\n' + ' --> '.join(nodes)

    def __iter__(self) -> Iterator[Node]:
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __len__(self) -> int:
        length = 0
        for _ in self:
            length += 1
        return length

    def traverse(self) -> None:
        for node in self:
            print(node.data)

    def insert_at_beginning(self, element: Node) -> None:
        element.next = self.start
        self.start = element

    def insert_at_end(self, element: Node) -> None:
        if self.start is  None:
            self.start = element
        
        else:
            for current_node in self:
                pass
            current_node.next = element

    def insert_after_node(self, element: Node, node_reference: Any) -> None:
        pass

    def delete_node(self, element_data: Any) -> None:
        if self.start is None:
            print('Empty linked list..')
            return
        

        
    def search(self, element_data: Any) -> Optional[Node]:
        # Returns the first node with matching data
        pass