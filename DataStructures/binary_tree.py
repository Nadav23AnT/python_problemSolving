class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    """
    Inserts a new node into the binary tree.

    Complexity:
    - Best case (balanced tree): O(log n)
    - Worst case (skewed tree): O(n)
    """
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root


def search(root, key):
    """
    Searches for a key in the binary tree.

    Complexity:
    - Best case (balanced tree): O(log n)
    - Worst case (skewed tree): O(n)
    """
    if root is None or root.data == key:
        return root
    if root.data < key:
        return search(root.right, key)
    return search(root.left, key)


def delete(root, key):
    """
    Deletes a node from the binary tree.

    Complexity:
    - Best case (balanced tree): O(log n)
    - Worst case (skewed tree): O(n)
    """
    if root is None:
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.data = minValue(root.right)
        root.right = delete(root.right, root.data)
    return root


def minValue(node):
    """
    Finds the minimum value in the binary tree.

    Complexity: O(log n)
    """
    current = node
    while current.left is not None:
        current = current.left
    return current.data


def preorder(root):
    """
    Pre-order traversal of a binary tree.

    Complexity: O(n)
    """
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    """
    In-order traversal of a binary tree.

    Complexity: O(n)
    """
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def postorder(root):
    """
    Post-order traversal of a binary tree.

    Complexity: O(n)
    """
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Example usage
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

result = search(root, 40)
if result is not None:
    print("Key found!")
else:
    print("Key not found!")

root = delete(root, 20)
print("Key deleted!")

print("Pre-order traversal:")
preorder(root)
print()

print("In-order traversal:")
inorder(root)
print()

print("Post-order traversal:")
postorder(root)
print()
