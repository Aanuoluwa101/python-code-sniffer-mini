from checkers import FunctionChecker, ClassChecker


rules = {
    "max_function_length": 4,
    "max_function_args_count": 2,
    "ensure_function_docstring": True
}

registered_checkers = [FunctionChecker, ClassChecker]
    