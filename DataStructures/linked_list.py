class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        # Time complexity: O(1)
        return self.head is None

    def insert(self, data):
        new_node = Node(data)

        if self.is_empty():
            # Time complexity: O(1)
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            # Time complexity: O(n), n = number of nodes in the linked list

    def delete(self, data):
        if self.is_empty():
            # Time complexity: O(1)
            return

        if self.head.data == data:
            self.head = self.head.next
            # Time complexity: O(1)
        else:
            current_node = self.head
            while current_node.next is not None and current_node.next.data != data:
                current_node = current_node.next
            if current_node.next is not None:
                current_node.next = current_node.next.next
            # Time complexity: O(n), n = number of nodes in the linked list

    def search(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
        # Time complexity: O(n), n = number of nodes in the linked list

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()
        # Time complexity: O(n), n = number of nodes in the linked list


# Test the linked list implementation
linked_list = LinkedList()

linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)

linked_list.display()  # Output: 10 20 30

linked_list.delete(20)

linked_list.display()  # Output: 10 30

print("Search result:", linked_list.search(30))  # Output: True
