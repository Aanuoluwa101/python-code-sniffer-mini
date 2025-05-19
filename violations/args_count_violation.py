from .violation import Violation


class ArgsCountViolation(Violation):
    def __init__(self, node, **kwargs):
        super().__init__(node)
        self.args_count = kwargs.get("args_count")
        self.max_args_count = kwargs.get("max_args_count")  # get from central config

    def show(self):
        return f"'{self.node.name}' at line {self.node.lineno} has more than {self.max_args_count} arguments: {self.args_count}"
