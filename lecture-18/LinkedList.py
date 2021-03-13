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

    # assume it has cycle
    def cycleLength(self):
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break

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

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertFirst(2)
    ll.insertFirst(3)
    ll.insertFirst(8)
    ll.insertFirst(12)
    ll.display()
    ll.insertAfter(5, 8)
    ll.display()
    # print(ll.removeFirst())
    # ll.display()
    # print(ll.removeLast())
    # ll.display()
    last = ll.find(2)
    start = ll.find(8)
    last.next = start

    print(ll.cycleLength())
