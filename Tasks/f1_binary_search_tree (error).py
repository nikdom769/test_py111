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
    global binary_tree, v_tree
    if not binary_tree:
        binary_tree['key'] = key
        binary_tree['value'] = value
        binary_tree['left'] = {} 
        binary_tree['right'] = {}
    else:
        node = binary_tree
        while node:
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
    del_node = binary_tree
    pred_node = binary_tree
    while del_node:
        if key == del_node['key']:
            if not del_node['left'] and not del_node['right']:
                old_node = (del_node['key'], del_node['value'])
                if not pred_node['left'] and not pred_node['right']:
                    clear()
                elif pred_node['left']['key'] == del_node['key']:
                    pred_node['left'] = {}
                elif pred_node['right']['key'] == del_node['key']:
                    pred_node['right'] = {}
                return old_node
            elif not del_node['right']:
                new_node = del_node['left'].copy()
                old_node = (del_node['key'], del_node['value'])
                pred_node['key'] = new_node['key']
                pred_node['value'] = new_node['value']
                pred_node['left'] = new_node['left']
                pred_node['right'] = new_node['right']
                return old_node
            else:
                pass
        elif key < del_node['key']:
            pred_node = del_node
            del_node = del_node['left']
        elif key > del_node['key']:
            pred_node = del_node
            del_node = del_node['right']
    return None


def find(key: Hashable) -> Optional[Any]:
    """
    Find value by given key in the BST
    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    global binary_tree, v_tree
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

