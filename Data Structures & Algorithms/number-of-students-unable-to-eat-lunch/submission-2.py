class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = len(students)
        counts = Counter(students)

        for s in sandwiches:
            if counts[s] > 0:
                result -= 1
                counts[s] -= 1
            else: 
                break
        return result
        