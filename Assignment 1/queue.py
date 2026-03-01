# Import the Node() class
from node import Node 

# Make the Queue() class
class Queue: 
    def __init__(self): 
        self.front = None 
        self.rear = None 

    # is_empty method
    def is_empty(self): 
        if self.front == None: 
            return True
        else:
            return False

    # enqueue method 
    def enqueue(self, data): 
        new_node = Node(data)
        # Makes sure this also counts as front if queue is empty before adding this node 
        if self.is_empty(): 
            self.front = new_node
        # This part makes the new node point to what the current rear is
        new_node.next = self.rear
        # Changes the rear to the new node now
        self.rear = new_node

    # dequeue method 
    def dequeue(self):
        if self.is_empty():
            return "Cannot complete operation - queue is empty"
        else: 
            # Saves current node before we update front node
            current_node = self.front
            # Update the front node to the 2nd node
            self.front = self.front.next
            return current_node.data

    # peek method 

    # __repr__ dunder method

# Example 

def main():
    # Initialize the queue 
    queue = Queue()

    print(queue.is_empty()) # True 

    queue.enqueue(1)
    print(queue.dequeue()) # 1
    print(queue.dequeue()) # Cannot complete operation - queue is empty

main()

