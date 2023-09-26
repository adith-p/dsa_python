# Linkedlist python


class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def insert_in_head(self, value):
        l = Node(value)
        l.next = self.head
        self.head = l

        self.n += 1

    def travese(self):
        if self.head == None:
            return "Empty List"
        curr = self.head
        result = ''
        while curr != None:
            result = result + f"{str(curr.data)}->"
            curr = curr.next
        return result[:-2]

    def append(self, value):
        l = Node(value)
        if self.head == None:
            self.head = l
            self.n += 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next

        curr.next = l
        self.n += 1

    def insert_middle(self, after, value):
        new_node = Node(value)

        curr = self.head
        while curr != None:
            if curr.data == after:
                new_node.next = curr.next
                curr.next = new_node
                self.n += 1
                return 0
            curr = curr.next
        print("empty list do something")

    def clear_list(self):
        self.head = None

    def delete_head(self):
        # 2->1->53->25->5
        if self.head == None:
            return 0
        self.head = self.head.next
        self.n -= 1
        # curr = self.head
        # self.head = curr.next
        # curr.next = None

    def delete_tail(self):
        if self.head == None:
            return 0

        curr = self.head
        # while curr.next != None:
        #     prev = curr
        #     curr = curr.next
        # prev.next = None
        # self.n -= 1
        while curr.next.next != None:
            """
                2->1->53->25->5
                stops at 53 since next of next of 53 is None 
                if total 5 elem stops at 3 : if 4 elem stops at 2
            """
            curr = curr.next
        curr.next = None
        self.n -= 1

    def delete_by_value(self, value):
        if self.head == None:
            return 0

        curr = self.head

        if curr.data == value:
            return self.delete_head()

        while curr != None:
            if curr.next == None:
                return "Item  not found"
            if curr.next.data == value:
                curr.next = curr.next.next
                return 0
            curr = curr.next

    def search(self, value):

        curr = self.head
        index = 0
        while curr != None:
            if curr.data == value:
                return index
            curr = curr.next
            index += 1
        return "Not Found"

    def __getitem__(self, index):
        curr = self.head
        i = 0
        while curr != None:
            if i == index:
                return curr.data
            i += 1
            curr = curr.next
        return "Not found"


l = LinkedList()

l.insert_in_head(5)
l.insert_in_head(25)
l.insert_in_head(53)
l.insert_in_head(1)
l.insert_in_head(2)

# l.insert_middle(value="Middle", after=5)

# l.append("Append2")
# l.append("Append3")

print(l.travese())
# l.delete_by_value(2)
# print(l.travese())
# print(l.search(255))
print(l[3])
