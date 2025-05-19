from abc import ABC, abstractmethod
import ast


class Violation(ABC):
    # perhaps load the config here
    def __init__(self, node: ast.AST , *args, **kwargs):
        if not node or not isinstance(node, ast.AST):
            raise ValueError("node must be an instance of ast.AST")
        self.node = node
        
    @abstractmethod
    def show(self) -> str:
        pass 

    def __str__(self):
        return f"- {self.__class__.__name__}: {self.show()}"