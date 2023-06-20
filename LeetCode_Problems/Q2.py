# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Implementation of the Solution class
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        curr_node_1 = list1
        curr_node_2 = list2
        newList = ListNode()
        curr = newList
        while curr_node_1 and curr_node_2:
            if (curr_node_1.val <= curr_node_2.val):
                curr.next = curr_node_1
                curr_node_1 = curr_node_1.next
            else:
                curr.next = curr_node_2
                curr_node_2 = curr_node_2.next
            curr = curr.next

        if curr_node_1:
            curr.next = curr_node_1
        if curr_node_2:
            curr.next = curr_node_2

        return newList.next

# Creating the first linked list: 1 -> 2 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Creating the second linked list: 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Creating an instance of the Solution class
solution = Solution()

# Testing the mergeTwoLists method
merged = solution.mergeTwoLists(list1, list2)

# Displaying the merged list
while merged:
    print(merged.val, end=" ")
    merged = merged.next