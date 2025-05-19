import ast 
from checkers.function_checker import FunctionChecker

with open("fail_sniff.py", "r") as f:  
    source = f.read()

tree = ast.parse(source)
config = {
            "max_function_length": 2,
            "max_function_args_count": 1,
            "ensure_docstring": True
        }
checker = FunctionChecker(tree, config)
checker.run()
print(checker.violations)