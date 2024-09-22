""" Программа для поиска LCA из n1 и n2, используя один обход
бинарного дерева
Она обрабатывает все случаи, даже если n1 или n2 отсутствуют в дереве
"""

# Узел бинарного дерева


class Node:

    # Конструктор для создания нового узла
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Эта функция возвращает указатель на LCA из двух заданных значений
# n1 и n2
# значение v1 устанавливается этой функцией как true, если найдено n1
# значение v2 устанавливается этой функцией как true, если найдено n2


def findLCAUtil(root, n1, n2, v):

    # Базовый вариант
    if root is None:
        return None

    # # ЕСЛИ n1 или n2 совпадают с ключом root, сообщите
    # о наличии, установив значение v1 или v2 как true и вернув
    # root (Обратите внимание, что если ключ является предком other, то
    # ключом-предком становится LCA)
    if root.key == n1:
        v[0] = True
        return root

    if root.key == n2:
        v[1] = True
        return root

    # Ищите ключи в левом и правом поддереве
    left_lca = findLCAUtil(root.left, n1, n2, v)
    right_lca = findLCAUtil(root.right, n1, n2, v)

    # Если оба приведенных выше вызова возвращают значение, отличное от NULL, то один ключ
    # присутствует в одном поддереве, а другой - в другом,
    # Таким образом, этот узел является LCA
    if left_lca and right_lca:
        return root

    # В противном случае проверьте, является ли левое поддерево или правое поддерево LCA
    return left_lca if left_lca is not None else right_lca


def find(root, k):

    # Базовый вариант
    if root is None:
        return False

    # Если ключ присутствует в корне, или в левом поддереве, или в правом
    # поддерево , возвращает true
    if (root.key == k or find(root.left, k) or
            find(root.right, k)):
        return True

    # Else возвращает значение false
    return False

# Эта функция возвращает LCA из n1 и n2 по значению, если оба
# n1 и n2 присутствуют в дереве, в противном случае возвращает None


def findLCA(root, n1, n2):

    # Инициализировать n1 и n2 как не посещенные
    v = [False, False]

    # Найдите lca для n1 и n2, используя технику, описанную выше.
    lca = findLCAUtil(root, n1, n2, v)

    # Возвращает LCA только в том случае, если в дереве присутствуют как n1, так и n2
    if (v[0] and v[1] or v[0] and find(lca, n2) or v[1] and
            find(lca, n1)):
        return lca

    # Else возвращает значение None
    return None


# Программа для тестирования вышеуказанной функции
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

lca = findLCA(root, 4, 5)

if lca is not None:
    print("LCA(4, 5) = ", lca.key)
else:
    print("Keys are not present")

lca = findLCA(root, 4, 10)
if lca is not None:
    print("LCA(4,10) = ", lca.key)
else:
    print("Keys are not present")
