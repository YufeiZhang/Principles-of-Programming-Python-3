class PriorityQueue():
    min_capacity = 10

    def __init__(self, capacity = min_capacity):
        self.min_capacity = capacity
        self.data = [None] * capacity
        self.length = 0
        self.record = {}

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def insert(self, element):
        datum = element[0]
        worth = element[1]
        if datum in self.record:
            self.update(datum, worth)
            return
        if self.length + 1 == len(self.data):
            self.resize(2 * len(self.data))
        self.length += 1
        self.data[self.length] = [datum, worth]
        self.record[datum] = self.length
        self.bubble_up(self.length)
        
    def delete(self):
        top_datum = self.data[1][0]
        del self.record[top_datum]
        self.data[1], self.data[self.length] = self.data[self.length],self.data[1]
        self.length -= 1
        if self.min_capacity <= self.length <= len(self.data)//4:
            self.resize(len(self.data)//2)
        self.bubble_down(1)
        return top_datum

    def update(self, datum, worth):
        i = self.record[datum]
        if worth > self.data[i][1]:
            self.data[i][1] = worth
            self.bubble_up(i)
        elif worth < self.data[i][1]:
            self.data[i][1] = worth
            self.bubble_down(i)
            self.bubble_up(i)

    def bubble_up(self, i):
        if i > 1 and self.data[i][1] > self.data[i//2][1]:
            self.data[i//2], self.data[i] = self.data[i], self.data[i//2]
            self.record[self.data[i//2][0]] = i//2
            self.record[self.data[i][0]] = i
            self.bubble_up(i//2)
            
    def bubble_down(self, i):
        child = 2 * i
        if child < self.length and self.data[child + 1][1] > self.data[child][1]:
            child += 1
        if child <= self.length and self.data[child][1] > self.data[i][1]:
            self.data[child], self.data[i] = self.data[i], self.data[child]
            self.record[self.data[child][0]] = child
            self.record[self.data[i][0]] = i
            self.bubble_down(child)

    def resize(self, new_size):
        self.data = list(self.data[:self.length + 1]) + [None] * (new_size - self.length - 1)

        
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
    
