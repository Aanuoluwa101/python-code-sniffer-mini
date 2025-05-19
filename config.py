from checkers import FunctionChecker, ClassChecker


checks = {
         "Function Check": {
            "description": "Checks the length and number of arguments passed to functions",
            "checker": FunctionChecker,
            "config": {
                "max_function_length": 4,
                "max_function_args_count": 2,
                "ensure_docstring": True
            }
        },
          "Class Check":{
            "description": "Checks that a class has docstring",
            "checker": ClassChecker,
            "config": {}
        }
    }
    

if __name__ == "__main__":
    print(type(FunctionChecker))