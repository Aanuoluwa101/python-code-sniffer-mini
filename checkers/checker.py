import ast
from abc import ABC, abstractmethod


class Checker(ABC):
    def __init__(self, tree: ast.AST, config):
        self.tree = tree
        self.config = config
        self.violations = []

    @abstractmethod
    def run(self, node: ast.AST):
        pass 