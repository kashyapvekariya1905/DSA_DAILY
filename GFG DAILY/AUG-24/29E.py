#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #Your code here
        slow = fast = head  # Initialize two pointers, slow and fast, at the head
        count=1
        while fast and fast.next:
            # Move slow one node forward
            slow = slow.next
            # Move fast two nodes forward
            fast = fast.next.next
            # If slow and fast meet, a loop exists
            if slow == fast:
                # Traverse the loop to find its length
                while slow.next != fast:
                    slow = slow.next
                    count += 1

                # Return the length of the loop
                return count

        # If no loop is found, return 0
        else:
          return 0
