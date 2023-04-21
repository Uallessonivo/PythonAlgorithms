from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head

    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
        else:
            break

        slow = slow.next

    return slow
