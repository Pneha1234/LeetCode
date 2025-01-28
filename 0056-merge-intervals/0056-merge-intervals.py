class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)
        n = len(sorted_intervals)
        result = []
        for i in range(n):
            print()
            if len(result) == 0:
                result.append(sorted_intervals[0])
            elif result[-1][1] < sorted_intervals[i][0]:
                result.append(sorted_intervals[i])
            else:
                result[-1][1] = max(sorted_intervals[i][1], result[-1][1])
        return result

        