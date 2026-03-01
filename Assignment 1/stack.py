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
            print("Cannot complete operation - stack is empty")
            return
        else: 
            # Saves current node before we update top
            current_top = self.top
            # Update the top to the node beneath
            self.top = self.top.next
            return current_top.data

    # peek method 

    # size method 

    # Make repr to print all the nodes
    def __repr__(self):
        print(self.top)
        ...
    

# Example 

def main(): 
    # Initialize a new stack
    stack = Stack()

    print(stack.is_empty()) # Returns True

    stack.__repr__()

    stack.pop() # Returns 'Cannot complete operation - stack is empty'

    stack.push(1)
    stack.push(2)
    print(stack.pop()) # 2
    print(stack.pop()) # 1
    print(stack.pop()) # Returns 'Cannot complete operation - stack is empty'

main()