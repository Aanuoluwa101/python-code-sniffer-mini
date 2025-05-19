from .violation import Violation


class NoDocstringViolation(Violation):
    def __init__(self, node, **kwargs):
        super().__init__(node)
        

    def show(self):
        return f"'{self.node.name}' has no docstring"
