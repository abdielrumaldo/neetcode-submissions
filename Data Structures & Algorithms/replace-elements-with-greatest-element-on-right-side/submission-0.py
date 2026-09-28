class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for i in range(len(arr)):
            j = i + 1
            val = -1
            while j < len(arr):
                val = max(val, arr[j])
                j += 1

            arr[i] = val

        return arr