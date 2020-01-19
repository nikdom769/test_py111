from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.
    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    d = [stairway[0], stairway[1]]
    for i in range(2, len(stairway)):
        d.append(min(d[i - 1], d[i - 2]) + stairway[i])
    #return d[-1] if d[-1] < d[-2] else d[-2] # позволит перепрыгнуть последнюю ступеньку
    return d[-1] # позволяет пройти 3 тест
