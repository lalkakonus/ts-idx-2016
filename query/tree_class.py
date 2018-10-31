class node(object):
    def __init__(self, priority): 
        self.priority = priority
        self.left = None
        self.right = None

    def go_to(self):
        pass

    def evaluate(self):
        pass

class word_node(node):
    def __init__(self, value, priority):
        super(word_node, self).__init__(4 + priority)
        self.value = value
        self.stream = None
        self.stream_value = 1
        self.position = 0

    def evaluate(self):
        if self.position < len(self.stream):
            return self.stream[self.position], True
        else:
            if self.stream:
                return self.stream[-1] + 1, False
            else:
                return 1, False

    def go_to(self, value):
        while self.position < len(self.stream):
            if self.stream[self.position] < value:
                self.position += 1
            else:
                break

class and_node(node):
    def __init__(self, priority):
        super(and_node, self).__init__(priority + 2)
    
    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()
        
        while left[0]!=right[0] and left[1] and right[1]:
            if left < right:
                self.left.go_to(right[0])
                left = self.left.evaluate()
            else:
                self.right.go_to(left[0])
                right = self.right.evaluate()
        
        valid = (left[0] == right[0]) and left[1] and right[1]
        value = max(left[0], right[0])

        return value, valid

    def go_to(self, pos):
        self.left.go_to(pos)
        self.right.go_to(pos)

class or_node(node):
    def __init__(self, priority):
        super(or_node, self).__init__(priority + 1)
        self.flag = 0


    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()

        if left[1] and not right[1]: 
            return left
        if right[1] and not left[1]:
            return right
        if left[1] and right[1]:
            return min(left[0], right[0]), True
        
        return max(left[0], right[0]), False

    def go_to(self, pos):
        self.left.go_to(pos)
        self.right.go_to(pos)

class not_node(node):
    def __init__(self, priority):
        super(not_node, self).__init__(priority + 3)
        self.position = 0
        self.max_pos = 0

    def evaluate(self):
        value, valid = self.right.evaluate()
        
        if self.position == (self.max_pos + 1):
            return self.position, False

        if valid == False:
            return self.position, True

        if self.position == value:
            return value + 1, False
        else:
            return self.position, True

    def go_to(self, pos):
        if pos <= (self.max_pos + 1):
            self.position = pos
        self.right.go_to(pos)

class tree(object):
    def __init__(self, node):
        self.root = node

    def print_tree(self):
        self.node.print_node()
