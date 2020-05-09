# Chained hashmap data structure made by Anirudh Lakra.

# Make sure the map stays fixed size otherwise search doesnt work.
class Map:

    def __init__(self, size):

        self.list = [None] * size
        self.size = size


    # Inserts value into hashmap.
    def insert(self, value):

        key = hash(value) % self.size
        if self.list[key] == None:
            entry = Entry(value)
            self.list[key] = entry

        # If there is already an entry at "key", set next of the entry
        # at "key" to value.
        else:
            cur_node = self.list[key]
            while cur_node.get_next() != None:
                cur_node = cur_node.get_next()
            cur_node.set_next(value)

        return key


    # Search for value in hashmap.a
    def search(self, value):

        key = hash(value) % size
        if self.list[key].get_value() == value:
            return True
        elif self.list[key] == None:
            return False

        # If there is a linked list at "key". Search through the
        # linked list until you find it or reach the end.
        cur_node = self.list[key]
        while cur_node.get_next() != None:
            if cur_node.get_value() == value:
                return True
            cur_node = cur_node.get_next()

        return False


    # Remove value from hashmap.
    def remove(self, value):

        key = hash(value) % self.size
        cur_node = self.list[key]

        # Look for value in linkedlist at "key".
        if cur_node.get_value() == value:

            # If there is a linked list at "key".
            if cur_node.get_next() != None:
                self.list[key] = cur_node.get_next()
                cur_node.set_next(None)

            # There was only 1 entry at "key", no linked list.
            else:
                self.list[key] = None
            return

        prev_node = cur_node
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
            if cur_node.get_value() == value:

                # If value is not found at the end.
                if cur_node.get_next() != None:
                    prev_node.set_next(cur_node.get_next())
                    cur_node.set_next(None)

                # Value is at end of linked list.
                else:
                    prev_node.set_next(None)
                    cur_node.set_next(None)
                return
        return "Not found"


    def print(self):
        for entries in self.list:
            if entries != None:
                cur_node = entries
                while cur_node:
                    print(cur_node.get_value(), end = ' ')
                    cur_node = cur_node.get_next()
                print()
            else:
                print(entries)

        

# Auxiliary class for each entry into the hashmap.
class Entry:

    def __init__(self, value=None, next=None):

        self.value = value
        self.next = next


    def get_value(self):

        return self.value


    def get_next(self):

        return self.next


    def set_next(self, value):

        entry = Entry(value)
        self.next = entry


def test_hashmap():

    hash_map = Map(10)
    hash_map.insert(10)
    hash_map.insert(23)
    hash_map.insert(45)
    hash_map.insert(57)
    hash_map.insert(45)
    hash_map.insert(10)
    hash_map.print()


test_hashmap()
    

