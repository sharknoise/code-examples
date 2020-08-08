"""https://ru.hexlet.io/challenges/python_oop_basics_tree_builder"""


class TreeBuilder:
    def __init__(self, initial_structure=[]):
        self.structure = initial_structure
        self._current_path = ''

    @property
    def structure(self):
        return self._structure

    @structure.setter
    def structure(self, value):
        self._structure = value

    def add(self, leaf_value):
        """Add a leaf to the current node."""
        first_part = 'self._structure'
        path_part = self._current_path
        append_part = '.append(leaf_value)'
        print(first_part + path_part + append_part)
        print(self.structure)
        eval(first_part + path_part + append_part)
    
    def __enter__(self):
        self._current_path = self._current_path + '[0]'

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._current_path = self._current_path[:-3]

# tree = TreeBuilder([1, 2, 3])
tree = TreeBuilder()
tree.add('1st')
tree.add('1bst')
with tree:
    tree.add('2nd')
    #with tree:
    #    tree.add('3rd')
    #tree.add('4th')
print(tree.structure)