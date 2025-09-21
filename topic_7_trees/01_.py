class Node:
    def __init__(self, key):
        self.left: Node | None = None
        self.right: Node | None = None
        self.val = key


def preorder_traversal(root):
    if root:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)


# Створення дерева
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Прямий обхід:")
preorder_traversal(root)


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

print("Центровий обхід:")
inorder_traversal(root)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)


print("Зворотний обхід:")
postorder_traversal(root)

