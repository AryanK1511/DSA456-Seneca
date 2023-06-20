# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        l1Str, l2Str = "", ""
        curr_node = l1
        while l1 is not None:
            l1Str += str(l1.val)
            l1 = l1.next
        while l2 is not None:
            l2Str += str(l2.val)
            l2 = l2.next
        totalSum = int(l1Str[::-1]) + int(l2Str[::-1])
        dummy = ListNode()
        curr_node = dummy
        for digit in str(totalSum)[::-1]:
            curr_node.next = ListNode(int(digit))
            curr_node = curr_node.next
        return dummy.next

# Testing the addTwoNumbers method
# Creating the first linked list: 2 -> 4 -> 3
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Creating the second linked list: 5 -> 6 -> 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Displaying the result
while result:
    print(result.val, end=" ")
    result = result.next
