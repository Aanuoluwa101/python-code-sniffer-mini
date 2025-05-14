from abc import ABC, abstractmethod


class Violation(ABC):
    def __init__(self, node_name: str, *args, **kwargs):
        if not node_name or not isinstance(node_name, str) or len(node_name.strip()) == 0:
            raise ValueError("node_name must be a non-empty string")
        self.node_name = node_name
        
    @abstractmethod
    def show(self) -> str:
        pass 

    def __str__(self):
        return f"- {self.__class__.__name__}: {self.show()}\n"