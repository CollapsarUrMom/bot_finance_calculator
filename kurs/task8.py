# Программа на Python для поиска LCA из n1 и n2, используя один
# обход бинарного дерева

# Узел бинарного дерева


class Node:

    # Конструктор для создания нового узла дерева
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Эта функция возвращает указатель на LCA из двух заданных
# значений n1 и n2
# Эта функция предполагает, что n1 и n2 присутствуют в
# Двоичном дереве


def findLCA(root, n1, n2):

    # Базовый вариант
    if root is None:
        return None

    # Если n1 или n2 совпадают с ключом root, сообщите
    # о наличии, вернув root (Обратите внимание, что если ключ является
    # предком other, то ключом-предком становится LCA
    if root.key == n1 or root.key == n2:
        return root

    # Ищите ключи в левом и правом поддеревьях
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    # Если оба приведенных выше вызова возвращают значение, отличное от NULL, то один ключ
    # присутствует в одном поддереве, а другой - в другом,
    # Таким образом, этот узел является LCA
    if left_lca and right_lca:
        return root

    # В противном случае проверьте, является ли левое поддерево или правое поддерево LCA
    return left_lca if left_lca is not None else right_lca


if __name__ == '__main__':
    
    # Давайте создадим бинарное дерево, приведенное в приведенном выше примере
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("LCA(4, 5) = ", findLCA(root, 4, 5).key)
    print("LCA(4, 6) = ", findLCA(root, 4, 6).key)
    print("LCA(3, 4) = ", findLCA(root, 3, 4).key)
    print("LCA(2, 4) = ", findLCA(root, 2, 4).key)
