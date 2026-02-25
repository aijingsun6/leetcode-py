from typing import List

class P1356:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def kf(v:int) -> tuple[int,int]:
            return (v.bit_count(),v)
        return list(sorted(arr,key=kf))

    def sortByBits2(self, arr: List[int]) -> List[int]:
        tmp = list(map(lambda v : (v.bit_count(),v), arr))
        tmp.sort()
        return list(map(lambda  x : x[1], tmp))



p = P1356()
arr = [1,2,3,4,5]
print(p.sortByBits2(arr))

