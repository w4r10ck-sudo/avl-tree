class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def insert(key, node):
    if node is None:
        return Node(key)
    elif key < node.key:
        node.left = insert(key, node.left)
    else:
        node.right = insert(key, node.right)
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBal(node)
    if balance > 1 and key < node.left.key:
        return RR(node)
    if balance < -1 and key > node.right.key:
        return LR(node)
    if balance > 1 and key > node.left.key:
        node.left = LR(node.left)
        return RR(node)
    if balance < -1 and key < node.right.key:
        node.right = RR(node.right)
        return LR(node)

    return node


def binary_search(node, key):
    if node is None:
        return None
    else:
        if key > node.key:
            binary_search(node.right, key)
        elif key < node.key:
            binary_search(node.left, key)
        else:
            print('{0} found'.format(node.key))


def getHeight(node):
    if not node:
        return 0
    else:
        return node.height


def getBal(node):
    if not node:
        return 0
    else:
        return getHeight(node.left) - getHeight(node.right)


def LR(node):
    n1 = node.right
    n2 = n1.left
    n1.left = node
    node.right = n2
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    n1.height = 1 + max(getHeight(n1.left), getHeight(n1.right))
    return n1


def RR(node):
    n1 = node.left
    n2 = n1.right
    n1.right = node
    node.left = n2
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    n1.height = 1 + max(getHeight(n1.left), getHeight(n1.right))
    return n1


def bfs(node):
    queue = [node]
    while queue:
        node = queue[0]
        queue = queue[1:]
        print(node.key, end=' ')
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=' ')
        inorder(node.right)


def preorder(node):
    if node:
        print(node.key, end=' ')
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key, end=' ')


root = Node(15)
root = insert(13, root)
root = insert(20, root)
root = insert(12, root)
root = insert(14, root)
root = insert(18, root)
root = insert(22, root)
root = insert(10, root)
root = insert(21, root)
root = insert(23, root)
root = insert(9, root)
root = insert(11, root)
print('BFS')
bfs(root)
print('\nInorder')
inorder(root)
print('\nPreorder')
preorder(root)
print('\nPostorder')
postorder(root)