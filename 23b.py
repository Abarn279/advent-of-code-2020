node_dict = {}

class SLLNode: 
    ''' Singly linked list node '''
    def __init__(self, nxt=None, data=None): 
        if nxt is None: 
            self.next = self
        else:
            self.next = nxt
        
        self.data = data
        node_dict[self.data] = self

    def insert_after(self, other_val):
        current_next = self.next
        self.next = SLLNode(current_next, other_val)
        return self.next

    def insert_bulk_after(self, ary):
        curr_next = self.next
        self.next = ary[0]
        ary[-1].next = curr_next

    def remove_range_after(self, amt):
        ''' Remove amt of nodes, after this one, returning the resulting array. '''
        nodes = []

        to_remove = self.next

        for n in range(amt):
            nodes.append(to_remove)
            to_remove = to_remove.next

        self.next = nodes[-1].next
        nodes[-1].next = None

        return nodes

    def find_destination(self, t = None):
        if t is None: 
            t = ((self.data - 2) % 1000000) + 1
        else: 
            t = ((t - 1) % 1000000) + 1
        return node_dict[t]

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

    def __eq__(self, other): 
        return self.data == other.data

    def __repr__(self):
        return str(self.data)

# My input
inp = '318946572'

# Build DLL
current = SLLNode(None, int(inp[0]))
nxt = current
for n in inp[1:]:
    nxt = nxt.insert_after(int(n))

for n in range(10, 1000001):
    nxt = nxt.insert_after(n)

for move in range(10000000):
    removed = current.remove_range_after(3)

    destination = current.find_destination()
    while destination in removed:
        destination = current.find_destination(destination.data - 1)

    destination.insert_bulk_after(removed)
    current = current.next

print(node_dict[1].next.data * node_dict[1].next.next.data)