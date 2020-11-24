import heapq
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next


s = Solution
ln11 = ListNode(1)
ln14 = ListNode(4)
ln11.next = ln14
ln15 = ListNode(5)
ln14.next = ln15
tl = [ln11]

tla = [1, 2]
tlb = [2]
print(tla+tlb+[3])
print([tla[-2]] + [tla[0]])

class TestNode():
    def __init__(self, x):
        self.val = x
        self.next = None

tna = TestNode(1)
tnb = TestNode(2)
tna.next = tnb

print(tna.next.val)