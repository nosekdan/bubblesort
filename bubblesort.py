from typing import TypeVar, MutableSequence, Callable
import operator

T = TypeVar("T")
Comparator = Callable[[T, T], bool]

def bubble_sort(arr: MutableSequence[T], cmp: Comparator = operator.lt) -> None:
    """Sort arr in-place using bubble sort.

    cmp(a, b) should return True when a < b (i.e. when a is considered
    "less than" b under the desired ordering). The function returns None.
    """
    n = len(arr)
    if n < 2:
        return None

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if cmp(arr[j + 1],arr[j]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break
        
a = [3, 4, 2, 1, 8, 7]
bubble_sort(a)
print(a)
# prints out: [1, 2, 3, 4, 7, 8]