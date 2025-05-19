from .checker import Checker
import ast
from violations import FunctionLengthViolation, ArgsCountViolation, NoDocstringViolation


class FunctionChecker(Checker):
    def __init__(self, tree, config):
        super().__init__(tree, config)

    def check_length(self, node):
        start_line = node.lineno
        end_line = node.end_lineno #max(getattr(child, 'end_lineno', child.lineno) for child in ast.walk(node) if hasattr(child, 'lineno'))
        length = end_line - start_line + 1
        max_function_len = self.config.get("max_function_length")


        if length > max_function_len:            
            violation = FunctionLengthViolation(node, length=length, start_line=start_line, max_function_len=max_function_len)
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
        self.check_arguments_count(node)
        if self.config.get("ensure_docstring"):
            self.check_docstring(node)

        self.generic_visit(node) 

    

