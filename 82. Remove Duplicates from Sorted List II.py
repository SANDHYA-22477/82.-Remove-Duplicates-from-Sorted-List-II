class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        current = dummy

        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                duplicate = current.next.val

                while current.next and current.next.val == duplicate:
                    current.next = current.next.next
            else:
                current = current.next

        return dummy.next