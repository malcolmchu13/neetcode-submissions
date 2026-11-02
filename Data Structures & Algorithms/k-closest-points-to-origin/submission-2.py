class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sorted_points = sorted(points, key=lambda row: row[0]**2 + row[1]**2)
        answer = []
        for i in range(k): 
            answer.append(sorted_points[i])

        return answer