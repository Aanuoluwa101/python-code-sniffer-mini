from violation import Violation


class FunctionLengthViolation(Violation):
    def __init__(self, node_name, **kwargs):
        super().__init__(node_name)
        self.length = kwargs.get("length")
        self.start_line = kwargs.get("start_line") 
        self.allowed_length = kwargs.get("allowed_length")

    def show(self):
        return f"'{self.node_name}' at line {self.start_line} is longer than {self.allowed_length}: {self.length}"
