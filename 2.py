
def combinationsum(candidate, target):
    result = []
    curr = []
    index = 0
    helper(candidate, target, index, result, curr)
    return result

def helper(candidate, target, currIndex, result, curr):
    if target == 0:
        result.append(list(curr))
        return
    elif target<0 or currIndex == len(candidate):
        return
    else:
        curr.append(candidate[currIndex])
        helper(candidate, target - candidate[currIndex], currIndex, result, curr)
        curr.pop()
        helper(candidate, target, currIndex + 1, result, curr)

combinationsum([1,2,3],5)                