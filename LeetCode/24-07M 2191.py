from typing import List


def sortJumbled(mapping: List[int], nums: List[int]) -> List[int]:
    return sorted(nums, key=lambda x: int("".join(chr(mapping[ord(c)-48]+48) for c in str(x))))

mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]
print(sortJumbled(mapping,nums))
mapping = [0,1,2,3,4,5,6,7,8,9]
nums = [789,456,123]
