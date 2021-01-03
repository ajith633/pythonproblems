from typing import List
import itertools


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        for tup in itertools.combinations_with_replacement(deliciousness,2):
            print(tup)
        return 1




if __name__ == '__main__':
    sol=Solution()
    sol.countPairs([1,1,3,5,7,9])