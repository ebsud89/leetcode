class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def oddEvenList(self, head: ListNode) -> ListNode:
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    while even and even_head:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head
    return head


print(oddEvenList(head))
