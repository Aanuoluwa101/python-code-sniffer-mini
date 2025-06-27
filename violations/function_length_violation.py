from .violation import Violation


class FunctionLengthViolation(Violation):
    def __init__(self, node, **kwargs):
        super().__init__(node)
        self.max_function_len = kwargs.get("max_function_len")

    def show(self):
        length = self.node.end_lineno - self.node.lineno
        return f"'{self.node.name}' at line {self.node.lineno} has more than {self.max_function_len} lines: {length}"
