"""
My little Stack
"""
from typing import Any

memory_steck = []

def push(elem: Any) -> None:
	"""
	Operation that add element to stack
	:param elem: element to be pushed
	:return: Nothing
	"""
	global memory_steck
	memory_steck.append(elem)
	#print(f"Добавлен {elem} в стек")
	return None


def pop() -> Any:
	"""
	Pop element from the top of the stack. If not elements - should return None.
	:return: popped element
	"""
	global memory_steck
	return memory_steck.pop() if memory_steck else None


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the stack without popping it.
	:param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
	:return: peeked element or None if no element in this place
	"""
	global memory_steck
	print(ind)
	return memory_steck[(len(memory_steck)-1) - ind] if memory_steck and ind < len(memory_steck) else None

def clear() -> None:
	"""
	Clear my stack
	:return: None
	"""
	global memory_steck
	memory_steck = []
	return None
