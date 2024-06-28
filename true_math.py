from math import inf
def divide(first, second):
    if second == 0:
        return str(float('inf')) + '  "inf" - это бесконечность по английски.'

    result = first/second
    return result
