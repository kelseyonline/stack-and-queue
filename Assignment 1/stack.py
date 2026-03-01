# Import the Node() class
from node import Node 

# Make the Stack() class 
class Stack: 
    def __init__(self):
        # Initialize this stack with no top yet
        self.top = None

    # is_empty method 
    def is_empty(self): 
        if self.top == None: 
            return True
        else:
            return False

    # push method 
    def push(self, data): 
        new_node = Node(data)
        # This part makes the new node point to what the current top is
        new_node.next = self.top
        # Changes the top to the new node now
        self.top = new_node

    # pop method 
    def pop(self):
        if self.is_empty():
            return "Cannot complete operation - stack is empty"
        else: 
            # Saves current node before we update top
            current_top = self.top
            # Update the top to the node beneath
            self.top = self.top.next
            return current_top.data

    # peek method 
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else: 
            print(self.top.data)
            return

    # size method 
    def size(self): 
        if self.is_empty(): 
            return "Stack is empty"
        else: 
            # Create counter
            size = 0 
            current_node = self.top
            while current_node is not None: 
                #print("Adding to counter")
                size += 1
                current_node = current_node.next
            return size 

    # Make repr to print all the nodes
    # I just modified this from the size() method
    def __repr__(self):
        if self.is_empty():
            return "Stack is empty"
        else: 
            print(f"Stack size: {self.size()}")
            current_node = self.top
            # I kept this outside of the while loop so I 
            # could add the 'top' designation in the printout
            print(f"{current_node.data} - top")
            current_node = current_node.next
            while current_node is not None: 
                print(current_node.data)
                current_node = current_node.next
    
# Example 

def main(): 
    # Initialize a new stack
    stack = Stack()

    print(stack.is_empty()) # Returns True

    stack.pop() # Returns 'Cannot complete operation - stack is empty'

    stack.push(1)
    stack.push(2)
    print(stack.pop()) # 2
    print(stack.pop()) # 1
    print(stack.pop()) # Returns 'Cannot complete operation - stack is empty'

    stack.push(1) 
    stack.peek() # 1
    stack.push(2)
    stack.push(3)

    print(stack.size()) # 3 

    print(stack.__repr__()) # This will show a printout of the stack using __repr__

main()