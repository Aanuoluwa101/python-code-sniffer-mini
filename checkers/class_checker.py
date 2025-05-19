from .checker import Checker
import ast
from violations import NoDocstringViolation

class ClassChecker(Checker):
    def __init__(self, tree, config):
        super().__init__(tree, config) 

    def check_docstring(self, node):
        if not ast.get_docstring(node):
            self.violations.append(NoDocstringViolation(node))   

    def visit_ClassDef(self, node):
        self.check_docstring(node)
        self.generic_visit(node) 
