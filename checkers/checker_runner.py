import ast
from checkers import FunctionChecker, ClassChecker


class CheckerRunner(ast.NodeVisitor):

    def __init__(self, tree, config):
        self.tree = tree
        self.config = config
        self.violations = []

    def run(self):
        self.visit(self.tree)  
    
    def visit_ClassDef(self, node):
        class_checker = ClassChecker(self.tree, self.config)
        class_checker.run(node)
        self.violations.extend(class_checker.violations)
        self.generic_visit(node) 

    def visit_FunctionDef(self, node):
        function_checker = FunctionChecker(self.tree, self.config)
        function_checker.run(node)
        self.violations.extend(function_checker.violations)
        self.generic_visit(node) 

    # def visit_Variable(self, node):
    #     pass 

    # def visit_Import(self, node):
    #     pass 

    # visit_Something 
    # visit_SomethingElse 
    # etc