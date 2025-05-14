from checker import Checker
import ast
from violations.function_length_violation import FunctionLengthViolation

class FunctionLengthChecker(Checker):
    def __init__(self):
        super().__init__()

    def visit_FunctionDef(self, node):
        start_line = node.lineno
        end_line = node.end_lineno #max(getattr(child, 'end_lineno', child.lineno) for child in ast.walk(node) if hasattr(child, 'lineno'))
        length = end_line - start_line + 1

        if length > self.max_length:
            allowed_length = self.config.get("max_function_length")
            violation = FunctionLengthViolation(node.name, length=length, start_line=start_line, allowed_length=allowed_length)
            self.violations.append(violation)

        self.generic_visit(node) 

    def run(self, source_code):
        tree = ast.parse(source_code)
        checker = FunctionLengthChecker()
        checker.visit(tree)

        return checker.violations