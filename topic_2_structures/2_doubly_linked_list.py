class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None


class DoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    # Додавання вузла на кінець списку
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Додавання вузла на початок списку
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    # Додавання вузла після заданого вузла
    def insert_after(self, prev_node, data):
        if not prev_node:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node

    # Додавання вузла перед заданим вузлом
    def insert_before(self, next_node, data):
        if not next_node:
            return
        new_node = Node(data)
        new_node.prev = next_node.prev
        next_node.prev = new_node
        new_node.next = next_node
        if new_node.prev:
            new_node.prev.next = new_node
        else:
            self.head = new_node

    def remove(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                    current_node.prev = None
                    current_node.next = None
                return True
            current_node = current_node.next
        return False

    def search(self, target_data):
        current_node = self.head
        while current_node:
            if current_node.data == target_data:
                return current_node
            current_node = current_node.next
        return None


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.push(0)
node_2 = dll.search(2)
if node_2:
    dll.insert_after(node_2, 2.5)
node_2_5 = dll.search(2.5)
if node_2_5:
    dll.insert_before(node_2_5, 2.25)
dll.remove(2.5)



