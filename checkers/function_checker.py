from checker import Checker
import ast
from violations.function_length_violation import FunctionLengthViolation
from violations.args_count_violation import ArgsCountViolation
from violations.no_docstring_violation import NoDocstringViolation

class FunctionChecker(Checker):
    def __init__(self):
        super().__init__()

    def check_length(self, node):
        start_line = node.lineno
        end_line = node.end_lineno #max(getattr(child, 'end_lineno', child.lineno) for child in ast.walk(node) if hasattr(child, 'lineno'))
        length = end_line - start_line + 1
        max_function_len = self.config.get("max_function_length")

        if length > max_function_len:            
            violation = FunctionLengthViolation(node.name, length=length, start_line=start_line, max_function_len=max_function_len)
            self.violations.append(violation)


    def check_arguments_count(self, node):
        arguments_count = len(node.args.args)
        arguments_count += 1 if node.args.vararg else 0
        arguments_count += 1 if node.args.kwarg else 0 
        
        max_args_count = self.config.get("max_function_args_count")
        if arguments_count > max_args_count:
            violation = ArgsCountViolation(node, args_count=arguments_count, max_args_count=max_args_count)
            self.violations.append(violation)   

    def check_docstring(self, node):
        if not ast.get_docstring(node):
            self.violations.append(NoDocstringViolation(node))   

    def visit_FunctionDef(self, node):
        self.check_length(node)
        self.check_arguments_count()
        self.check_docstring
        self.generic_visit(node) 

    def run(self, source_code):
        tree = ast.parse(source_code)
        checker = FunctionChecker()
        checker.visit(tree)

        return checker.violations