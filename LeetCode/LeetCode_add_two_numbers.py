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
            if ptr1.next != None and ptr2.next != None:
                    ptr3.next = ListNode()

            ptr1 = ptr1.next
            ptr2 = ptr2.next
            ptr3 = ptr3.next
            print()

        return l3



if __name__ == "__main__":
    sol = Solution()

    l1 = ListNode(val=2)
    l1.next = ListNode(val=4)
    l1.next.next = ListNode(val=3)

    l2 = ListNode(val=5)
    l2.next = ListNode(val=6)
    l2.next.next = ListNode(val=4)

    # print(l1)
    # print(l2)

    ans = sol.addTwoNumbers(l1, l2)
    print(ans)