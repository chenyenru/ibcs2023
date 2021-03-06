# data_strutures/queue.py
"""
FIFO. First In First Out
"""


from typing import Iterator


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        # a node pointing to the next node
        self.next: Node = None
        pass


class Queue:
    def __init__(self) -> None:
        self._head: Node = None
        self._tail: Node = None
        self._length: int = 0
        self._iter: Node = None

    def enqueue(self, data: int) -> None:
        n = Node(data)
        if self._tail == None:
            # when this is our first element
            self._head = n
            self._tail = n
        else:
            self._tail.next = n
            self._tail = n
        self._length += 1

    def dequeue(self) -> int:
        if self._head is None:
            return None

        data = self._head.data
        self._head = self._head.next
        self._length -= 1

        # takes care of the case when dequeueing the last node, where the tail may still be the node
        if self._head is None:
            self._tail = None

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


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)

    print(f"Queue's Length = {len(q)}")
    print(6 in q)

    print(str(q))

    print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
    print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
    print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
    print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
    print(f"Dequeue: {q.dequeue()}\t Length: {len(q)}")
