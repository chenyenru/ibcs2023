# data_strctures/stack.py
"""
FILO data structure. First In Last Out
"""


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        # a node pointing to the next node
        self.next: Node = None
        pass


class Stack:
    def __init__(self) -> None:
        self._head: Node = None
        self._length = 0
        self._iter: None = None

    def push(self, data: int) -> None:
        """
        Put things on the stack
        """
        n = Node(data)  # starts a node object
        n.next = self._head  # sets the next to the current head
        self._head = n  # updates the head to be the current node added
        self._length += 1

    def pop(self) -> int:
        """
        Pop things off the stack
        """
        if self._head is None:
            return None

        tmp = self._head.data  # before we move head, we need to know the head there
        self._head = self._head.next
        self._length -= 1
        return tmp

    def __len__(self) -> int:
        return self._length

    def __str__(self) -> str:
        # s = "["
        # n = self._head
        # while n is not None:
        #     s += f"{n.data}"
        #     n = n.next
        #     if n is not None:
        #         s += ", "
        # s += "]"

        s = []
        n = self._head
        while n is not None:
            s.append(n.data)
            n = n.next
        s.reverse()
        output = ', '.join(str(e) for e in s)
        return output

    def __iter__(self):
        self._iter = self._head  # points back to the front of our stack
        return self

    def __next__(self):
        if self._iter is None:
            raise StopIteration  # tells Python that we're done with the list
        tmp = self._iter.data  # get the data
        self._iter = self._iter.next  # return iterator
        return tmp

    def __contains__(self, data: int) -> bool:
        for d in self:
            if d == data:
                return True
        return False


if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(6)
    s.push(10)
    s.push(15)
    for x in s:
        print(x)

    print(10 in s)

    # print(f"Length: {s.__len__}")
    print(s)
    print(f"Pop: {s.pop()}\t Length: {len(s)}")
    print(f"Pop: {s.pop()}\t Length: {len(s)}")
    print(f"Pop: {s.pop()}\t Length: {len(s)}")
    print(f"Pop: {s.pop()}\t Length: {len(s)}")
    print(f"Pop: {s.pop()}\t Length: {len(s)}")
