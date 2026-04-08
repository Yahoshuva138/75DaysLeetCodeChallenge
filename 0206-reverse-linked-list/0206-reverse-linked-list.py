class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next   # store next node
            curr.next = prev        # reverse link
            prev = curr             # move prev forward
            curr = next_temp        # move curr forward
        
        return prev