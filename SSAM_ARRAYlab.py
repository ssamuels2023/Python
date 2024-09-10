## Sophie Samuels
## COP3410
## LAB 8: Chapter 6: Stacks
## 04/10/2024

class ArrayStack:
    '''LIFO Stack implementation using a Python list as underlying storage.'''

    def __init__ (self, maxlen):
        '''Q2(pt1): Modify the stack ADT file to introduce a limitation on the stack's capacity. This
            adjustment involves setting a maximum number of elements (maxlen) that the stack
            can hold, where maxlen is a new parameter in the stack's constructor. To
            accommodate this feature, pre-allocate a list with a length equal to the stack's
            maximum capacity upon initialization...'''
        '''Create an empty stack.'''
        self._maxlen = maxlen
        self._data = [None] * maxlen # pre-allocated list with max capacity
        self._size = 0 #current num of elements in stack

    def __len__ (self):
        '''Return the number of elements in the stack.'''
        return self._size

    def is_empty(self):
        '''Return True if the stack is empty.'''
        return self._size == 0

    def push(self, e):
        '''Add element e to the top of the stack.'''
        if self._size == self._maxlen: #check if stack is full
            raise Full('Stack is full')
        self._data[self._size] = e #assign current size as new element index
        self._size += 1

    def top(self):
        '''Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        '''
        if self.is_empty( ):
            raise Empty( 'Stack is empty' )
        return self._data[self._size - 1] # the last item in the list

    def pop(self):
        '''Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        '''
        if self.is_empty():
            raise Empty('Stack is empty')
        self._size -= 1
        return self._data.pop() # remove last item from list

    def __str__(self): #this method allows us to print the objects of stack class
        return str(self._data[:self._size])

    def clear_all(self):
        '''remove all elements from the stack using recursion'''
        '''Implement a recursive method named clear_all within the stack ADT class, to
        remove all elements from the stack. This method should utilize a recursive strategy
        to empty the stack, calling itself until the stack is fully cleared. Ensure to define a
        base case for the recursion to prevent infinite recursive calls.'''
        if not self.is_empty():
            self.pop() #remove top element
            self.clear_all() #clear remaining elements recursively

class Empty(Exception): # Defines an Empty class as a trivial subclass of the Python Exception class.
    '''Error attempting to access an element from an empty container.'''
    pass

class Full(Exception): # Defines a Full class as a trivial subclass of the Python Exception class.
    '''Error attempting to add an element to a full container.'''
    '''Q2(pt2)...Should an attempt be made to push an
    additional element onto the stack when it is already at full capacity, your
    implementation must throw a FullException.'''
    pass

def is_palindrome(str, size):
    '''Q1: Use the stack ADT from the class lectures to create a function. This function should
    accept a single string as input and return a Boolean value (True or False) indicating
    whether the given string is a palindrome. Implement this functionality by leveraging
    the operations of the stack, such as push and pop, to compare the characters from
    the beginning and end of the string.'''
    stack_size = size // 2
    stack = ArrayStack(stack_size)

    n = len(str) #assign length of str to 'n'
    middle = n // 2 #find middle

    for i in range(middle):
        stack.push(str[i]) #push first half of str onto stack

    start = middle if n % 2 == 0 else middle + 1 #ensure str skips middle char if length is odd

    for i in range(start, n):
        if stack.pop() != str[i]: #compare second half of str with stack
            return False #not palindrome

    return True #is palindrome

def reverse_file(filename):
    '''Overwrite given file with its contents line-by-line reversed.'''
    print("reversefile executing")
    S = ArrayStack()
    original = open(filename)
    for line in original:
        for i in line:
            S.push(i) # we will re-insert newlines when writing
    original.close( )
    # now we overwrite with contents in LIFO order
    output = open(filename, 'w' ) # reopening file overwrites original
    while not S.is_empty( ):
        output.write(S.pop( )) # re-insert newline characters
    output.close( )

print(is_palindrome("runner", 6))
print(is_palindrome("kayak", 5))
print(is_palindrome("helloolleh", 10))

if __name__ == "__main__":
    stack = ArrayStack(20)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print("Stack after adding 1,2,3,4:", stack)
stack.clear_all()
print("Stack after clearing function:", stack)
print("Is the stack empty now?", stack.is_empty())