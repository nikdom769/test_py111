"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Hashable, Any, Optional, Tuple
# import networkx as nx

binary_tree = {}


def insert(key: Hashable, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree
    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    global binary_tree
    if not binary_tree:
        #  если дерево пустое
        binary_tree['key'] = key
        binary_tree['value'] = value
        binary_tree['left'] = {} 
        binary_tree['right'] = {}
    else:
        node = binary_tree
        while node:
            # размещение вершины в зависимости от значения ключа
            if key > node['key']:
                if node['right']:
                    node = node['right']
                else:
                    node['right']['key'] = key
                    node['right']['value'] = value
                    node['right']['left'] = {}
                    node['right']['right'] = {}
                    return None
            elif key < node['key']:
                if node['left']:
                    node = node['left']
                else:
                    node['left']['key'] = key
                    node['left']['value'] = value
                    node['left']['left'] = {}
                    node['left']['right'] = {}
                    return None
            elif key == node['key']:
                node['value'] = value
                return None


def remove(key: Hashable) -> Optional[Tuple[Hashable, Any]]:
    """
    Remove key and associated value from the BST if exists
    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    global binary_tree
    del_node = binary_tree # удаляемый узел
    pred_node = binary_tree #  предок удаляемого узла
    while del_node:
        if key == del_node['key']:
            # проверка условий для удаляемого узла
            old_node = (del_node['key'], del_node['value'])
            new_branch = {}
            left_branch = del_node['left'].copy()
            right_branch = del_node['right'].copy()
            if left_branch or right_branch:
                # лист или нет
                if left_branch['right']:
                    right_bot_node = left_branch['right']
                    pred_right_bot_node = left_branch
                    while right_bot_node['right']:
                        pred_right_bot_node = right_bot_node
                        right_bot_node = right_bot_node['right']
                    new_branch['key'] = right_bot_node['key']
                    new_branch['value'] = right_bot_node['value']
                    new_branch['right'] = right_branch
                    pred_right_bot_node['right'] = right_bot_node['left']
                    new_branch['left'] = left_branch
                elif left_branch:
                    left_branch['right'] = right_branch
                    new_branch = left_branch
                else:
                    new_branch = right_branch
            else:
                new_branch = {}
            if pred_node['key'] == del_node['key']:
                # если удаляемый узел - корень
                binary_tree = new_branch
                return old_node
            elif pred_node['left']['key'] == del_node['key']:
                # если удаляемый узел является левым
                pred_node['left'] = new_branch
                return old_node
            elif pred_node['right']['key'] == del_node['key']:
                # если удаляемый узел является правым
                pred_node['right'] = new_branch
                return old_node
        elif key < del_node['key']:
            # поиск удаляемого узла слева
            pred_node = del_node
            del_node = del_node['left']
        elif key > del_node['key']:
            # поиск удаляемого узла справа
            pred_node = del_node
            del_node = del_node['right']
    return None


def find(key: Hashable) -> Optional[Any]:
    """
    Find value by given key in the BST
    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    global binary_tree
    node =  binary_tree
    while node:
        if key == node['key']:
            return node['value']
        elif key < node['key']:
            node = node['left']
        elif key > node['key']:
            node = node['right']
    #print(key)
    else:
        raise KeyError


def clear() -> None:
    """
    Clear the tree
    :return: None
    """
    global binary_tree
    binary_tree = {}
    return None

