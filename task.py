class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            return temp
        elif not root.right:
            temp = root.left
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


def min_value_of_tree(root: Node):
    return min_value_node(root).val

def max_value_of_tree(root: Node):
    return max_value_node(root).val

def sum_of_tree(root: Node):
    sum = root.val
    if root.left:
        sum += sum_of_tree(root.left)
    if root.right:
        sum += sum_of_tree(root.right)
    return sum


def main():
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    root = delete(root, 7)
    print(root)

    print(f"Найбільше значення в дереві: {min_value_of_tree(root)}")
    print(f"Найменше значення в дереві: {max_value_of_tree(root)}")
    print(f"Сума всіх значень у дереві: {sum_of_tree(root)}")


if __name__ == '__main__':
    main()