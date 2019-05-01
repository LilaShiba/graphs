class Node():

    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        # if there is already data
        if self.data:
            # left side
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # right side
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        # if there is no data
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def find(self,data):
        if data == self.data:
            return True
        elif self.data:
            if data < self.data:
                if self.left == None:
                    return False
                return self.left.find(data)
            elif data > self.data:
                if self.right == None:
                    return False
                return self.right.find(data)

    def make_array(self, arr):
        if self.left:
            self.left.make_array(arr)
        arr.append(self.data)
        if self.right:
            self.right.make_array(arr)
        return arr





root = Node(100)
root.insert(98)
root.insert(50)
root.insert(1984)
root.insert(143)
root.insert(54)
root.insert(2001)
root.insert(501)
#root.print_tree()
print(root.find(501))
print(root.make_array(arr=[]))
