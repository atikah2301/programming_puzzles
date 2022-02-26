# Medium difficulty

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {str(self.next)}"

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        ptr1 = l1
        ptr2 = l2
        ptr3 = l3
        carry = False

        while ptr1 != None or ptr2 != None:
            summand1 = 0 if ptr1 == None else ptr1.val
            summand2 = 0 if ptr2 == None else ptr2.val
            print(f"{summand1} + {summand2}", end=" ")

            summed = summand1 + summand2
            summed += 1 if carry else 0
            print(f"= {summed} because we carried the 1 from before") if carry else print(f"= {summed}, nothing carried from before")
            carry = False if summed < 10 else True
            print(f"Carry for the next sum? {carry}")

            ptr3.val = summed if summed < 10 else summed-10
            print(f"ptr3 takes value {ptr3.val}")

            if ptr1 != None:
                if ptr1.next != None:
                    ptr3.next = ListNode()
            if ptr2 != None:
                if ptr2.next != None:
                    ptr3.next = ListNode()
            if carry == True:
                ptr3.next = ListNode(val=1)

            ptr1 = ptr1.next if ptr1 != None else None
            ptr2 = ptr2.next if ptr2 != None else None
            ptr3 = ptr3.next
            print(l3)
            print()

        return l3



if __name__ == "__main__":
    sol = Solution()

    def make_linked_list(vals=[0]):
        l = ListNode()
        ptr = l
        for i in range(len(vals)):
            ptr.val = vals[i]
            if i != len(vals)-1:
                ptr.next = ListNode()
            ptr = ptr.next
        return l

    # l1 = make_linked_list([2,4,3])
    # l2 = make_linked_list([5,6,4])
    l1 = make_linked_list([9,9,9,9])
    l2 = make_linked_list([9,9,9,9,9,9,9])
    # Expected answer: 10,009,998 = 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1 -> None

    # print(l1)
    # print(l2)

    ans = sol.addTwoNumbers(l1, l2)
    print(ans)