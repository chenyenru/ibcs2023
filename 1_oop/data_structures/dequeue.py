# data_structures/dequeue.py
"""
- Combination of Queue and Stack
- Double ended Queue
- FILO + FIFO
"""


from typing import Iterator


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        # a node pointing to the next node
        self.next: Node = None
        self.prev: Node = None


class Dequeue:
    def __init__(self) -> None:
        self._head: Node = None
        self._tail: Node = None
        self._length: int = 0
        self._iter: Node = None

    def append(self, data: int) -> None:
        """
        尾部插入
        """
        n = Node(data)
        if self._tail == None:
            # when this is our first element
            self._head = n
            self._tail = n
        else:
            self._tail.next = n
            n.prev = self._tail
            self._tail = n
        self._length += 1

    def prepend(self, data: int) -> None:
        """
        頭部插入
        1. create node
        2. if head is None
        3. point node at head
        4. point head.prev at node
        5. move head to node
        """
        n = Node(data)  # starts a node object
        n.next = self._head  # sets the next to the current head

        if self._head:
            self._head = n
            self._tail = n
        else:
            self._head.prev = n
            self._head = n  # updates the head to be the current node added
        self._length += 1

    def delete_first(self) -> int:
        """
        頭部刪除
        """
        if self._head is None:
            return None

        data = self._head.data
        self._head = self._head.next
        if self._head:
            self._head.prev = None
        else:
            self._tail = None
        self._length -= 1

        # takes care of the case when dequeueing the last node, where the tail may still be the node

        return data

    def delete_last(self) -> int:
        """
        尾部刪除
        """
        if not self._tail:
            return None

        data = self._tail.data
        self._tail = self._tail.prev

        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._tail = self._tail.prev

        self._length -= 1
        return data

    def __len__(self):
        return self._length

    def __iter__(self) -> Iterator:
        self._iter = self._head
        return self

    def __next__(self) -> int:
        if self._iter is None:
            raise StopIteration  # tells Python that we're done with the list
        tmp = self._iter.data  # get the data
        self._iter = self._iter.next  # return iterator
        return tmp

    def __reversed__(self) -> Iterator:
        def reverse_iterator():
            r_iter = self._tail
            while r_iter is not None:
                yield r_iter.data
                r_iter = r_iter.prev
        return reverse_iterator()

    def __contains__(self, data: int) -> bool:
        for d in self:
            if d == data:
                return True
        return False

    def __str__(self):
        s = "["
        for i, d in enumerate(self):
            if i > 0:
                s += f"{str(d)}"
        s += "]"
        return s


q = Dequeue()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

print(f"Queue's Length = {len(q)}")
print(6 in q)

print(str(q))

print("Forwards")
for d in q:
    print(d)

print("Reversed")
for d in reversed(q):
    print(d)

# print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
# print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
# print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
# print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
# print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
