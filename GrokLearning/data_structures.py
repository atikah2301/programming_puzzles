# data structures
# Nodes


class Node:
    """
    An object for storing a single node of a linked list
    Models 2 attributes: data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"


class LinkedList:
    """
    Singly linked list
    Methods:
        Search for a key, search(key) -- done
        Insert data at a destination, insert(data, destination) -- done
        Remove data by key, remove(key) -- done
        Remove data at a destination, remove_at()
        Return data at a destination, data_at()
        Reverse order of nodes, reverse()
        Prepend data, prepend(data) -- done
        Check if empty, is_empty() -- done
        Length of list, size() -- done

    """

    def __init__(self):
        self.head = None  # needed for list traversal, using head as reference point

    def __repr__(self):
        """
        Returns a string representation of the linked list.
        Takes O(n) time (linear time)
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:  # Tail is defined as a node with no reference
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node
        return "->".join(nodes)

    def search(self, key):
        """
        Retrieve the first node containing data that matches the search key.
        Returns "None" if not found.
        Takes O(n) time (linear time) to complete.
        """
        current = self.head
        while current:
            if current.data is key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, destination):
        """
        Inserts a new Node containing data at the destination (a targeted, indexed position on the linked list).
        Indexing begins from 0.
        Insertion takes O(1) constant time, but position finding takes O(n) linear time.
        So overall time for insertion operation is O(n) linear time.
        """
        if destination is 0:
            self.prepend(data)  # inserting before the Head is same as prepending
        if destination > 0:
            current = self.head  # start counting from the Head
            new_node = Node(data)
            distance = destination  # distance = destination - current = destination - 0 = destination

            while distance > 1:  # don't decrease distance from target to 0, so that we have access to both refs needed
                current = current.next_node
                distance -= 1

            behind = current  # arrived at a position behind the destination
            ahead = current.next_node

            behind.next_node = new_node  # link the behind node's reference to the inserted node
            new_node.next_node = ahead  # link the new node's reference to the node ahead

    def remove(self, key):
        """
        Remove the first instance of specified data from the linked list.
        Cannot use search() method,
        since we would not be able to re-link the references of the nodes adjacent to the removed node,
        since our list is only singly linked not doubly linked.
        """
        current = self.head
        previous = None

        while current:
            if current.data == key and current is self.head:
                self.head = current.next_node
                break
            elif current.data == key:
                previous.next_node = current.next_node
                break
            else:
                previous = current
                current = current.next_node

        return current

    def is_empty(self):
        return self.head is None  # return true if the head is empty

    def size(self):
        """
        Returns the number of nodes in the linked list
        Takes O(n) time to complete (linear time, i.e. scales with length of list)
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node  # use a Node attribute since LinkedList().head is a Node
        return count

    def prepend(self, *data):
        """
        Prepends new node containing data at the head of the list.
        Takes O(1) time (constant time, because operation is the same regardless of list length)
        """
        for data in reversed(data):
            new_node = Node(data)
            new_node.next_node = self.head  # let the new node refer to the first node, the head
            self.head = new_node  # let the new node take the position as head of the list


l = LinkedList()
l.prepend(3,7,10,11)
l.insert(4,2)  # insert node with data "4" at index 2
# print(l.head)
# print(l.size())
l.remove(7)
print(l)

