import heapq

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        answer = []

        while len(nums) > 1:
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums)
            answer.append(bob)
            answer.append(alice)

        return answer