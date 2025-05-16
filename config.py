from checkers.function_checker import FunctionChecker
from checkers.class_checker import ClassChecker


checks = [
        {
            "name": "Function Check",
            "description": "Checks the length and number of arguments passed to functions",
            "checker": FunctionChecker,
            "config": {
                "max_function_length": 40,
                "max_function_args_count": 4,
                "ensure_docstring": True
            }
        },
        {
            "name": "Class Check",
            "description": "Checks that a class has docstring",
            "checker": ClassChecker,
            "config": {}
        },
    ]