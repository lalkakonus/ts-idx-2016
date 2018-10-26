import re

class node(object):

    def __init__(self, class_type, value=None, priority=0, left=None, right=None):
        self.value = value
        self.class_type = class_type
        self.priority = priority
        self.left = left
        self.right = right

    def add_right(self, node):
        self.right = node

    def add_left(self, node):
        self.left = node

    def get_priority(self):
        return self.priority

    def set_prioirity(self, priority):
        self.priority = priority

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_type(self):
        return self.class_type

    def set_type(self, class_type):
        self.class_type = class_type

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
        
def tokenize(query):
    tmp_list = re.findall(r'\w+|[\(\)\|&!]', query)
    token_list = []
    priority = 0
    for raw_token in tmp_list:
        if re.match('\w+', raw_token):
            token_list.append(node('w', raw_token, priority + 4))
        elif raw_token == '(':
            priority += 5
        elif raw_token == ')':
            priority -= 5
        elif raw_token == '|':
            token_list.append(node('|', raw_token, priority + 1))
        elif raw_token == '&':
            token_list.append(node('&', raw_token, priority + 2))
        elif raw_token == '!':
            token_list.append(node('!', raw_token, priority + 3))
   
    return  token_list

def parse_list(token_list):
   
    if len(token_list) == 1:
        return token_list[0]
    
    pos = 0
    min_priority = token_list[0].get_priority()
    for i, token in enumerate(token_list[1:]):
        if token.get_priority() <= min_priority:
            min_priority = token.get_priority()
            pos = i + 1

    if token_list[pos].class_type == '!':
        left = None
    else:
        left = parse_list(token_list[:pos])
    right = parse_list(token_list[pos + 1:])

    node = token_list[pos]
    node.add_left(left)
    node.add_right(right)

    return node


def parse(query):
    query = query.replace(' ', '')
    token_list = tokenize(query)
    root = parse_list(token_list)
    root.print_node()

# a = 'a & !(b | c)'
# parse(a)
