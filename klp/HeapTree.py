class HeapTree:
    def __init__(self, max):
        self.tree = []
        self.max = max
        self.currentSize = 0

    def checkParent(self, index):
        if index == 0:
            return

        parentVal = self.tree[int((index-1)/2)][0]
        childVal = self.tree[index][0]

        if childVal > parentVal:
            self.tree[int((index-1)/2)], self.tree[index] = self.tree[index], self.tree[int((index-1)/2)]
            self.checkParent(int((index-1)/2))

    def heapify(self, index):
        left = 2 * (index + 1) - 1
        right = 2 * (index + 1)

        if left >= self.currentSize:
            # has no child
            return

        elif right >= self.currentSize:
            # has only left child
            if self.tree[index][0] < self.tree[left][0]:
                self.tree[index], self.tree[left] = self.tree[left], self.tree[index]
                return

            else:
                return

        else:
            # has both childs
            if (self.tree[index][0] < self.tree[left][0]) and (self.tree[index][0] < self.tree[right][0]):
                if self.tree[left][0] < self.tree[right][0]:
                    self.tree[index], self.tree[right] = self.tree[right], self.tree[index]
                    self.heapify(right)
                else:
                    self.tree[index], self.tree[left] = self.tree[left], self.tree[index]
                    self.heapify(left)

            elif self.tree[index][0] < self.tree[right][0]:
                self.tree[index], self.tree[right] = self.tree[right], self.tree[index]
                self.heapify(right)

            elif self.tree[index][0] < self.tree[left][0]:
                self.tree[index], self.tree[left] = self.tree[left], self.tree[index]
                self.heapify(left)

            else:
                return

    def insert(self, node):
        if self.currentSize >= self.max:
            if self.tree[0][0] < node[0]:
                return
            else:
                self.pop()

        self.tree.append(node)
        self.currentSize += 1
        self.checkParent(self.currentSize-1)

    def pop(self):
        if self.currentSize == 0:
            print('heap is empty')
            return None

        returnVal = self.tree[0]
        self.tree[0], self.tree[self.currentSize-1] = self.tree[self.currentSize-1], self.tree[0]
        self.tree = self.tree[:-1]
        self.currentSize -= 1
        self.heapify(0)
        return returnVal
