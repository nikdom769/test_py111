"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any

memory_prior_queue = {}

def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue
    :param elem: element to be added
    :return: Nothing
    """
    global memory_prior_queue
    if priority in memory_prior_queue:
        memory_prior_queue[priority].append(elem)
    else:
        memory_prior_queue[priority] = [elem]
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.
    :return: dequeued element
    """
    global memory_prior_queue
    if memory_prior_queue:
        priority_min = min(memory_prior_queue)
        data = memory_prior_queue[priority_min].pop(0)
        if not memory_prior_queue[priority_min]:
            del memory_prior_queue[priority_min]
        return data
    else:
        return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it
    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global memory_prior_queue
    return memory_prior_queue[priority][ind] if memory_prior_queue\
            and  memory_prior_queue[priority]\
            and ind < len(memory_prior_queue[priority]) - 1 else None


def clear() -> None:
    """
    Clear my queue
    :return: None
    """
    global memory_prior_queue
    memory_prior_queue = {}
    return None

