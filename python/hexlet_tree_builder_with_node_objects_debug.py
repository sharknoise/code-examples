"""https://ru.hexlet.io/challenges/python_oop_basics_tree_builder"""


class TreeBuilder:
    def __init__(self, initial_structure=[]):
        self._structure = initial_structure
        self._target_for_add = self

    @property  # getter
    def structure(self):
        return self._structure

    @structure.setter
    def structure(self, value):
        self._structure = value

    def add(self, leaf_value):
        """Add to the current node."""
        self._target_for_add.append(leaf_value)
        print('added to target, target is now', self._target_for_add, 'tree is now', self.structure)
            
    def append(self, leaf_value):
        """Add to base level."""
        self._structure.append(leaf_value)
        print('appended to', self._target_for_add, 'tree is now', self._structure)
    
    def __enter__(self):
        print('entering context')
        self._target_for_add = Node(self._target_for_add)
        print('target changed to', self._target_for_add)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('parent when exiting context', self._target_for_add.parent_link)
        if self._target_for_add:
            self._target_for_add.parent_link.append(self._target_for_add)
            print('tree structure when exiting context', self._structure)
            print('target structure when exiting context',  self._target_for_add)
        self._target_for_add = self._target_for_add.parent_link


class Node(list):
    def __init__(self, parent_link, *args):
        initial_value = list(args)
        self.parent_link = parent_link
        self.extend(initial_value)
        print('creating a node', self)


# tree = TreeBuilder([1, 2, 3])
tree = TreeBuilder()
tree.add('1st')
with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
    tree.add('4th')
    with tree:
        pass
print(tree.structure)