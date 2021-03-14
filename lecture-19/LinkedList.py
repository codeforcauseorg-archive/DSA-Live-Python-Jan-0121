class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # O(1)
    def insertFirst(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    # O(N)
    def insertLast(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            return
        temp = self.head
        # make sure temp reaches last node
        while temp.next != None:
            temp = temp.next
        temp.next = node

    def find(self, target):
        temp = self.head
        while temp != None:
            if temp.val == target:
                return temp
            temp = temp.next
        return None

    # after should be present
    def insertAfter(self, val, after):
        temp = self.find(after)
        originalNext = temp.next
        node = Node(val)
        temp.next = node
        node.next = originalNext

    # O(1)
    def removeFirst(self):
        prev = self.head
        self.head = prev.next
        prev.next = None
        return prev.val

    def removeLast(self):
        if self.head == None:
            return None

        # One element
        if self.head.next == None:
            removed = self.head.val
            self.head = None
            return removed

        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        removed = temp.next.val
        temp.next = None
        return removed

    def hasCycle(self):
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    def findCycle(self):
        length = 0
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                length = self.cycleLength(slow)
                break
        return self.findStart(length)

    def findStart(self, length):
        p1, p2 = self.head, self.head
        while length > 0:
            p2 = p2.next
            length -= 1
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    def cycleLength(self, slow):
        temp = slow
        length = 0
        while True:
            temp = temp.next
            length += 1
            if temp == slow:
                break
        return length

    # O(N)
    def middle(self):
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow.val

    # O(N)
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end="->")
            temp = temp.next
        print('None')

    def reverse(self):
        p, c, n = None, self.head, None

        while c is not None:
            n = c.next
            c.next = p
            p = c
            c = n
        self.head = p

    def reverseKElements(self, k):
        if k <= 1 or self.head is None:
            return

        c, p = self.head, None

        while True:
            lastNodePrevPart = p
            lastNodeSubList = c

            next = None

            i = 0

            # reverse k nodes
            while c is not None and i < k:
                n = c.next
                c.next = p
                p = c
                c = n
                i += 1

            if lastNodePrevPart is not None:
                lastNodePrevPart.next = p
            else:
                # first sublist condition
                self.head = p

            lastNodeSubList.next = c

            if c is None:
                break
            p = lastNodeSubList

        return

if __name__ == '__main__':
    ll = LinkedList()
    for i in range(1, 10):
        ll.insertLast(i)
    ll.display()
    # last = ll.find(8)
    # start = ll.find(4)
    # last.next = start
    # print(ll.findCycle().val)
    # ll.reverse()
    # ll.display()
    ll.reverseKElements(3)
    ll.display()
