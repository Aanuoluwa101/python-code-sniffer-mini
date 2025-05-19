from .violation import Violation


class FunctionLengthViolation(Violation):
    def __init__(self, node, **kwargs):
        super().__init__(node)
        self.length = kwargs.get("length")
        self.max_function_len = kwargs.get("max_function_len")

    def show(self):
        return f"'{self.node.name}' at line {self.node.lineno} has more than {self.max_function_len} lines: {self.length}"
