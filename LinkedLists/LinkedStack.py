

class Node:
    """LIFO Stack implementation using singly linked list for storage"""
    def __init__(self, element, next):
        self._element = element #Reference adding element
        self._next = next #Reference next element


class LinkedStack:
    def __init__(self):
        """Create empty stack"""
        self._head = None #Reference to head node
        self._size = 0 # Number of Stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size
    
    def is_empty(self):
        """Return True if stack is empty"""
        return self._size == 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = Node(e, self._head) #create and link a new node
        self._size+=1

    def top(self):
        """Return the element at the top of stack, but don't remove.
        Raise Empty exception if the stack is empty.
        """

        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element
    
    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO)."""
        if self.is_empty():
            raise Exception('Stack is empty')
        answer = self._head._element
        self._head = self._head._next #bypass the former top now
        self._size -=1

        return answer
    




        

