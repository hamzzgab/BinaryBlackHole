from src.main.linked_list.singly.node import Node


class LinkedListOperations:

    @staticmethod
    def merge(l1, l2):
        head = ptr = Node()
        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        ptr.next = l1 or l2
        return head.next

    @staticmethod
    def reverse(l1):
        prev, curr = None, l1
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
