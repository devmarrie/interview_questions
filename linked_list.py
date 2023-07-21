# define the node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# define the linked list
class LinkedList:
    def __init__(self):
        self.head = None
    
    """functions to append into the linked list"""
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
    """Append before"""
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    """Delete a linked list"""
    def delete(self, data):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        curr_node = self.head
        while curr_node.next:
            if curr_node.next.data == data:
                curr_node.next == curr_node.next.next
                return
            curr_node = curr_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print("None")

if __name__ == '__main__':
    my_linked_lst = LinkedList()
    my_linked_lst.append(10)
    my_linked_lst.append(20)
    my_linked_lst.append(30)

    my_linked_lst.display()

    my_linked_lst.prepend(5)
    my_linked_lst.prepend(15)

    my_linked_lst.display()

    my_linked_lst.delete(20)

    my_linked_lst.display()