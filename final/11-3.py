class PriorityQueue():
    def __init__(self):
        self.data = []
        self.length = {}
        self.record = {}

    def is_empty(self):
        return self.length == 0

    def insert(self, element):
        self.data.append(element)
        self.record[element[0]] = element[1]
        self.data = self.reorder()

    def delete(self):
        out = self.data.pop()
        del(self.record[out[0]])
        self.length -= 1
        return out[0]

    def reorder(self):
        self.length = len(self.record)
        self.data = sorted(self.record.items(), key = lambda x:(x[1], x[0]))
        return self.data


if __name__ == '__main__':
    pq = PriorityQueue()
    L = [('A', 13), ('B', 13), ('C', 4), ('D', 15), ('E', 9), ('F', 4), ('G', 5), ('H', 14),
         ('A', 4), ('B', 11), ('C', 15), ('D', 2), ('E', 17),
         ('A', 8), ('B', 14), ('C',12), ('D', 9), ('E', 5),
         ('A', 6), ('B', 16)]
    for e in L:
        pq.insert(e)
    for i in range(8): print(pq.delete(), end=' ')
    print()
    print(pq.is_empty())
