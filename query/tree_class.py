class node(object):
    def __init__(self, class_type, value=None, priority=0,
                 left=None, right=None, evaluate=None, go_to=None, 
                 position=0, stream=None, stream_value=1):

        self.value = value
        self.class_type = class_type
        self.priority = priority
        self.left = left
        self.max_pos = 100
        self.right = right
        self.evaluate = evaluate
        self.go_to = go_to
        self.position = position
        self.stream = stream
        self.stream_value = stream_value

    def print_node(self):
        print 'value [' + self.value + '] class {' + self.class_type + '}'
        if self.left is not None:
            print 'left: ', self.left.get_value()
        if self.right is not None:
            print 'right: ', self.right.get_value()
        
        if self.left is not None:
            self.left.print_node()

        if self.right is not None:
            self.right.print_node()

class tree(object):
    def __init__(self, node):
        self.root = node

    def print_tree(self):
        self.node.print_node()
