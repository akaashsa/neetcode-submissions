# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is at the end of the first half

        # 2. Push second half onto stack
        stack = []
        cur = slow.next
        slow.next = None          # <-- cut the list here!
        while cur:
            stack.append(cur)
            cur = cur.next

        # 3. Merge: interleave head-half with popped nodes
        cur = head
        while stack:
            nxt = cur.next        # save the next first-half node
            node = stack.pop()
            cur.next = node
            node.next = nxt
            cur = nxt             # advance to the saved node