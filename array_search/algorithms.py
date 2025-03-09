def binary_search(list, element):
    print(f"{list}  {element} binaria")
    left = 0
    right = len(list) - 1
    while left <= right:
        middle: int = (right + left) // 2
        if list[middle] == element:
            return middle
        if list[middle] < element:
            left = middle + 1
        else:
            right = middle - 1
    return -1
def linear_search(list, element):
    print(f"{list}  {element} lineal")
    for i in range(len(list)):
        if list[i] == element:
            return i
    return -1
def ternary_search(list, element):
    print(f"{list}  {element} ternaria")
    left = 0
    right = len(list) - 1
    while left <= right:
        middleleft = left + (right - left) // 3
        middleright = right - (right-left) // 3
        if list[middleleft] == element:
            return middleleft
        if list[middleright] == element:
            return middleright
        if element < list[middleleft]:
            right = middleleft-1
        elif element > list[middleright]:
            left = middleright+1
        else:
            left = middleleft + 1
            right = middleright - 1
    return -1