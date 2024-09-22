# Программа на Python для поиска наименьшего общего предка в двоичном дереве
# O(n) решение для нахождения LCS из двух заданных значений n1 и n2

# Узел двоичного дерева
class Node:
    # Конструктор для создания нового двоичного узла
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Находит путь от корневого узла к заданному корню дерева.
# Сохраняет путь в виде списка path[], возвращает значение true, если путь существует
# в противном случае значение false
def findPath(root, path: list[bool], k):

    # Базовый вариант
    if root is None:
        return False

    # Хранить этот узел в виде вектора пути. Узел будет
    # удален, если он не находится в пути от корня до k
    path.append(root.key)

    # Посмотрите, совпадает ли k с ключом root
    if root.key == k:
        return True

    # Проверьте, находится ли k в левом или правом поддереве
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right != None and findPath(root.right, path, k))):
        return True

    # Если в поддереве, имеющем корень root, его нет, удалите
    # root из пути и верните значение False

    path.pop()
    return False


    # Возвращает значение LCA, если в данном дереве присутствуют узлы n1, n2
    # двоичное дерево, в противном случае возвращает значение -1
def findLCA(root, n1, n2):

    # Для сохранения путей к n1 и n2 из корневого каталога
    path1 = []
    path2 = []

    # Найдите пути от корня к n1 и от корня к n2.
    # Если n1 или n2 отсутствуют , верните значение -1
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

    # Сравните пути, чтобы получить первое различное значение
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]


# Программа-драйвер для тестирования вышеуказанной функции
if __name__ == '__main__':
    
    # Давайте создадим бинарное дерево, показанное на диаграмме выше
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("LCA(4, 5) = %d" % (findLCA(root, 4, 5,)))
    print("LCA(4, 6) = %d" % (findLCA(root, 4, 6)))
    print("LCA(3, 4) = %d" % (findLCA(root, 3, 4)))
    print("LCA(2, 4) = %d" % (findLCA(root, 2, 4)))

# Этот код предоставлен Никхилом Кумаром Сингхом (ник zuck_007).
