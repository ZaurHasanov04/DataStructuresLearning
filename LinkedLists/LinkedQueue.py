from LinkedStack import Node

#Node is same principle in implementations of LinkedLists

class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size
    
    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head._element # front aligned with head of list
    
    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        ans = self._head._element
        self._head = self._head._next
        self._size -=1
        if self.is_empty(): # special case as queue is empty
            self._tail = None # removed head had been the tail
        return ans

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = Node(e, None) # node will be new tail node
        if self.is_empty():
            self._head = newest #special case : previously empty
        else:
            self._tail._next = newest
        self._tail = newest # update reference to tail node
        self._size +=1        