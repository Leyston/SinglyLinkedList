class Node:

    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.ref = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while current_node is not None and position + 1 != index:
                position = position + 1
                current_node = current_node.ref

            if current_node is not None:
                new_node.ref = current_node.ref
                current_node.ref = new_node
            else:
                print("Index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.ref:
            current_node = current_node.ref

        current_node.ref = new_node

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while (current_node != None and position != index):
                position = position + 1
                current_node = current_node.ref

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

        # Method to remove first node of linked list

    def remove_first_node(self):
        if (self.head == None):
            return

        self.head = self.head.ref

        # Method to remove last node of linked list

    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        while (current_node.ref.ref):
            current_node = current_node.ref

        current_node.ref = None

        # Method to remove at given index

    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while (current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.ref

            if current_node != None:
                current_node.ref = current_node.ref.ref
            else:
                print("Index not present")

        # Method to remove a node from linked list

    def remove_node(self, data):
        current_node = self.head

        while (current_node != None and current_node.ref.data != data):
            current_node = current_node.ref

        if current_node == None:
            return
        else:
            current_node.ref = current_node.ref.ref

        # Print the size of linked list

    def sizeOfLL(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size = size + 1
                current_node = current_node.ref
            return size
        else:
            return 0

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty ")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
