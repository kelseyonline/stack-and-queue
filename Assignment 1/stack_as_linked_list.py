class Node: 
    def __init__(self, data): 
        self.data = data # Stores value of node 
        self.next = None # Pointer to the next node 

class Stack: 
    def __init__(self): 
        self.top = None # None when it first gets created

    # is_empty() method 
    def is_empty(self):
        return self.top is None

    # Push operation 
    def push(self, data): 
        new_node = Node(data) # Create new node 
        new_node.next = self.top # Make new node point to current node 
        self.top = new_node # Update the top to be new node 

    # Pop operation 
    def pop(self): 
        if self.is_empty(): 
            return "Stack is empty, cannot pop"
        
        popped_node = self.top # Get top node

        self.top = self.top.next # Update the top to return the next node 

        return popped_node.data # Return data of the popped node 
    
    # Peek operation 
    def peek(self): 
        if self.is_empty():
            return "Stack is empty, cannot peek"
        
        return self.top.data # Return the data of the top node 
    
    # Return the size of the stack 
    def size(self): 
        current = self.top 

        count = 0 
        
        while current: 
            count += 1
            current = current.next 

        return count 
    
# Example usage of stack 
if __name__ == "__main__":
    my_stack = Stack()

    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    print("Top element:", my_stack.peek())
    print("Stack side:", my_stack.size())

    print("Popped element:", my_stack.pop())
    print("Stack size after pop:", my_stack.size())