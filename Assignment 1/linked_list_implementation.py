# Create Node class 
class Node: 
    # Constructor to initialize a node with data
    # and set next to None
    def __init__(self, data): 
        # Store the data 
        self.data = data 

        # Initialize next as None
        self.next = None 

# Create LinkedList class 
class LinkedList: 
    # Constructor to initialize linked list with 
    # head node as None 
    def __init__(self):
        # Initialize head as none
        self.head = None

    # Create append method 
    def append(self, data): 
        # Create a new node with given data 
        new_node = Node(data)

        # If list is empty, set head to new node 
        if self.head is None: 
            self.head = new_node
            return 
    
        # Start traversal from the head 
        last = self.head 

        # Traverse until last node 
        while last.next: 
            last = last.next 

        # Set the last node's next to the new node 
        last.next = new_node 

    # Create print method 
    def print_list(self): 
        # Start from head node 

        current = self.head 

        # Traverse the list 
        while current: 
            # Print the data 
            print(current.data, end="->")

            # Move to the next node 
            current = current.next 

        # Print None at the end 
        print("None") 

    # Create a method to insert at beginning
    def insert_at_beginning(self, data): 
        # Create a new node with the given data 
        new_node = Node(data) 

        # Set new node's next to current head 
        new_node.next = self.head 

        # Update head to the new node 
        self.head = new_node 

    # Create a method to insert node after given node
    def insert_after(self, prev_node, new_data):
        # Check if prev_node is None: 
        if prev_node is None: 
            print("The given previous node cannot be None.")
            return 
        
        # Create a new node with the given data 
        new_node = Node(new_data)

        # Make the new node's next point to the previous node's next 
        new_node.next = prev_node.next

        # Make the previous node's next point to the new node 
        prev_node.next = new_node 

    # Create a method to delete the node from the beginning 
    def delete_from_beginning(self): 
        # If the list is empty, return 
        if self.head is None: 
            return 
        
        # Store the current head in a temp variable 
        temp = self.head 

        # Update the head to the next node 
        self.head = temp.next 

        # Free the old head 
        temp = None

    # Create a method to delete the node from the end 
    def delete_from_end(self): 
        # If the list is empty, return 
        if self.head is None: 
            return 
        
        # If there's only one node, delete it 
        if self.head.next is None: 
            self.head = None 
            return 
        
        # Initialize second_last to traverse the list 
        second_last = self.head

        # Traverse until the second to last node 
        while second_last.next.next: 
            second_last = second_last.next

        # Set second last node's next to None 
        second_last.next = None 

    # Create a method to delete a specific node with the given key 
    def delete_by_key(self, key):
        # Start from the head node
        temp = self.head 

        # If head node holds the key 
        if temp is not None and temp.data == key: 
            # Update head 
            self.head = temp.next 

            # Free the old head 
            temp = None 
            return 
        
        # Initialize prev to None for traversal 
        prev = None 

        # Traverse to find the key 
        while temp is not None and temp.data != key:
            # Keep track of previous node 
            prev = temp 

            # Move to the next node 
            temp = temp.next 

        # If key is not found, return 
        if temp is None: 
            return 
        
        # Unlink the node from the list 
        prev.next = temp.next 

        # Free the node 
        temp = None 


if __name__ == "__main__":
    # Initialize the linked list 
    llist = LinkedList()

    # Insert elements 
    llist.insert_at_beginning(10)
    llist.append(20)
    llist.insert_after(llist.head, 15)

    # Print the list 
    llist.print_list()

    # Delete from beginning 
    llist.delete_from_beginning()

    # Print updated list 
    llist.print_list()

    # Delete from end 
    llist.delete_from_end()

    # Print updated list 
    llist.print_list() 