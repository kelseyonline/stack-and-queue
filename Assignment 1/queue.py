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
            self.front = self.rear = new_node
        else: 
            # This part makes the current rear point to the new rear 
            self.rear.next = new_node
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
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else: 
            # Saves current node before we update front node
            return self.front.data
        
    # size method 
    def size(self): 
        if self.is_empty(): 
            return "Queue is empty"
        else: 
            # Create counter
            size = 0 
            current_node = self.front
            while current_node is not None: 
                #print("Adding to counter")
                size += 1
                current_node = current_node.next
            return size

    # __repr__ dunder method
    def __repr__(self):
        if self.is_empty():
            return "Queue is empty"
        else: 
            print(f"Queue size: {self.size()}")
            current_node = self.front
            # I kept this outside of the while loop so I 
            # could add the 'top' designation in the printout
            print(f"{current_node.data} - front")
            current_node = current_node.next
            while current_node is not None: 
                print(current_node.data)
                current_node = current_node.next
            return

# Example 

def main():
    # Initialize the queue 
    queue = Queue()

    print(queue.is_empty()) # True 

    queue.enqueue(1)
    print(queue.dequeue()) # 1
    print(queue.dequeue()) # Cannot complete operation - queue is empty

    queue.enqueue(1)
    print(queue.peek()) # 1 

    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.size()) # 2
    queue.enqueue(4)
    queue.enqueue(5)

    print(queue.__repr__())

main()

