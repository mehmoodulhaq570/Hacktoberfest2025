import math

def jump_search(arr, target):
    """
    Jump Search Algorithm
    ---------------------
    Works on sorted arrays.
    Time Complexity: O(√n)
    Space Complexity: O(1)

    Parameters:
        arr (list): Sorted list of elements
        target (any): Element to search for
    Returns:
        int: Index of target element if found, else -1
    """
    n = len(arr)
    step = int(math.sqrt(n))  # optimal jump size
    prev = 0

    # Jump ahead while target is greater than the last element of current block
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search within the identified block
    while prev < n and arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    # If found
    if prev < n and arr[prev] == target:
        return prev

    return -1


# ------------------------------
# Example Usage
# ------------------------------
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 13, 17, 21, 25, 29, 33, 37]
    target = int(input("Enter element to search: "))

    result = jump_search(arr, target)

    if result != -1:
        print(f"✅ Element {target} found at index {result}")
    else:
        print(f"❌ Element {target} not found in array")
