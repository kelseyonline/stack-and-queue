class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Queue: 
    def __init__(self): 
        self.front = None # Points to head
        self.rear = None # Points to the rear
        self._size = 0 

    # Enqueue operation 
    def enqueue(self, item): 
        new_node = Node(item)

        if self.rear is None: # If Q is empty 
            self.front = self.rear = new_node 
        else: 
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
        print(f"Enqueued: {item}")
    
    def dequeue(self): 
        if self.is_empty(): 
            print("Queue is empty, cannot dequeue.")
            return None 

        temp = self.front 

        self.front = self.front.next

        if self.front is None: # If Q becomes empty after dequeue
            self.rear = None

        self._size -= 1

        print(f"Dequeued: {temp.value}")
        return temp.value
    
    # Peek operation 
    def peek(self): 
        if self.is_empty(): 
            print("Queue is empty")
            return None 
        
        return self.front.value
    
    # Check if queue is empty 
    def is_empty(self): 
        return self.front is None 
    
    # Get size of queue 
    def size(self):
        return self._size
    
    # Display the queue 
    def display(self): 
        if self.is_empty():
            print("Queue is empty.")
            return 
        
        current = self.front

        print("Queue:", end=" ")

        while current: 
            print(current.value, end="->")
            current = current.next

        print("None")

# Run an example 
if __name__ == "__main__":
    my_queue = Queue()

    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)

    my_queue.display()

    my_queue.dequeue()

    my_queue.display()

    print(my_queue.peek())