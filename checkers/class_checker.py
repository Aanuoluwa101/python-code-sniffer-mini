from .checker import Checker
import ast
from violations import NoDocstringViolation

class ClassChecker(Checker):
    def __init__(self, tree, config):
        super().__init__(tree, config) 

    def check_docstring(self, node):
        if not ast.get_docstring(node):
            self.violations.append(NoDocstringViolation(node))   

    # define methods that do some other checks on classes here. 
    # methods should have only one parameter: node

    def run(self, node):
        self.check_docstring(node)
        # call the other methods you've defined here