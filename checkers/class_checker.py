from checker import Checker
import ast
from violations.no_docstring_violation import NoDocstringViolation

class ClassChecker(Checker):
    def __init__(self):
        super().__init__() 

    def check_docstring(self, node):
        if not ast.get_docstring(node):
            self.violations.append(NoDocstringViolation(node))   

    def visit_ClassDef(self, node):
        self.check_docstring
        self.generic_visit(node) 

    def run(self, source_code):
        tree = ast.parse(source_code)
        checker = ClassChecker()
        checker.visit(tree)

        return checker.violations