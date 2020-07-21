class Node(list):
    def __init__(self, *args):
        initial_value = list(args)
        self.extend(initial_value)

test = Node(1,2,3)

print(test)