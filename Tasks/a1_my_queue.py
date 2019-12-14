"""
My little Queue
"""
from typing import Any

memory_queue = []

def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue
    :param elem: element to be added
    :return: Nothing
    """
    global memory_queue
    memory_queue.append(elem)
    print(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.
    :return: dequeued element
    """
    global memory_gueue
    return memory_queue.pop(0) if memory_queue else None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it
    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    print(ind)
    return memory_queue[ind] if memory_queue and ind < len(memory_queue) - 1 else None


def clear() -> None:
    """
    Clear my queue
    :return: None
    """
    global memory_queue
    memory_queue = []
    return None

