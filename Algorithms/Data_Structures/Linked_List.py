# Made by Anirudh Lakra
# Doubly linked list with some basic functions.

# Linked list class that stores reference to head.
class LinkedList:

    def __init__(self, head=None):

        self.head = head


    # Set new head of linked list.
    # @params: head = new head of linked list
    def set_head(self, head):

        after = self.head.get_next()
        self.head = head
        self.head.set_next(after)


    # Print linked list.
    def print(self):

        cur = self.head
        print("Head: " + str(cur.get_value()))

        while cur.get_next() != None:
            cur = cur.get_next()
            print("At: " + str(cur.get_value()))


    # Add value to linked list.
    # @params: value = value to be added.
    def add(self, value):

        node = Node(value, None)
        cur = self.head
        while cur.get_next() != None:
               cur = cur.get_next()
        cur.set_next(node)


# Helper class for each element of linked list.
class Node:

    def __init__(self, value=None, next=None):

        self.value = value
        self.next = next


    def get_value(self):

        return self.value


    def get_next(self):

        return self.next


    def set_value(self, value):

        self.value = value


    def set_next(self, next):

        self.next = next


def test_linked_list():

    head = Node(10)
    linked_list = LinkedList(head)
    linked_list.add(20)
    linked_list.add(-2032)
    linked_list.add(-320.42)
    linked_list.print()

test_linked_list()



    
