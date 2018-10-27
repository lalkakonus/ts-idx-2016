# node_functions module
# Kononov Sergey BD-21

# WORD_FUNCTION
def evaluate_word(self):
    if self.position < len(self.stream):
        return self.stream[self.position], True
    else:
        return self.stream[-1] + 1, False

def go_to_word(self, value):
    while self.stream[self.position] < value and self.position < len(self.stream):
        self.position += 1


# AND_FUNCTION
def evaluate_and(self):
    left = self.left.evaluate()
    right = self.right.evaluate()
    
    valid = (left[0] == right[0]) and left[1] and right[1]
    value = max(left[0], right[0])

    return value, valid

def go_to_and(self, pos):
    self.left.go_to(pos)
    self.right.go_to(pos)


# OR_FUNCTION
def evaluate_or(self):
    left = self.left.evaluate()
    right = self.right.evaluate()

    if left[1] and not right[1]:
        return left
    if right[1] and not left[1]:
        return right
    if left[1] and right[1]:
        return min(left[0], right[0]), True
    
    return max(left[0], right[0]), False

def go_to_or(self, pos):
    self.left.go_to(pos)
    self.right.go_to(pos)


# NOT_FUNCTION
def evaluate_not(self):
    right = self.right.evaluate()
    
    if self.position == (self.max_pos + 1):
        return self.position, False
    
    if self.positon == right:
        return right, False
    else:
        return self.position, True

def go_to_not(self, pos):
    if pos <= (self.max_pos + 1):
        self.position = pos
    self.right.go_to(pos)

functions = {'w': [evaluate_word, go_to_word],
             '!': [evaluate_not, go_to_not],
             '&': [evaluate_and, go_to_and],
             '|': [evaluate_or, go_to_or]}
