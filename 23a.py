class DLLNode: 
    ''' Doubly linked list node '''
    def __init__(self, nxt=None, prev=None, data=None): 
        if nxt == None: 
            self.next = self
        else:
            self.next = nxt
        if prev == None:
            self.prev = self
        else:
            self.prev = prev

        self.data = data

    def insert_after(self, other_val):
        current_next = self.next
        self.next = DLLNode(current_next, self, other_val)
        current_next.prev = self.next
        return self.next

    def insert_bulk_after(self, ary):
        curr_next = self.next

        self.next = ary[0]
        ary[0].prev = self

        curr_next.prev = ary[-1]
        ary[-1].next = curr_next

    def remove_range_after(self, amt):
        ''' Remove amt of nodes, after this one, returning the resulting array. '''
        nodes = []

        to_remove = self.next
        to_remove.prev = None

        for n in range(amt):
            nodes.append(to_remove)
            to_remove = to_remove.next

        self.next = nodes[-1].next
        nodes[-1].next.prev = self
        nodes[-1].next = None

        return nodes

    def find_destination(self):
        c = self.next
        t = ((self.data - 2) % 9) + 1
        while True:
            if c.data == t:
                return c
            if c is self:
                t -= 1
                if t == 0: t = 9
            c = c.next

    def get_order(self):
        o = self.next
        while o.data != 1:
            o = o.next
        c = o.next
        s = ""
        while c is not o:
            s += str(c.data)
            c = c.next
        return s

    def __repr__(self):
        return str(self.data)

# My input
inp = '318946572'

# Build DLL
current = DLLNode(None, None, int(inp[0]))
nxt = current
for n in inp[1:]:
    nxt = nxt.insert_after(int(n))

for move in range(100):
    removed = current.remove_range_after(3)
    destination = current.find_destination()
    destination.insert_bulk_after(removed)
    current = current.next

print(current.get_order())