import ast
from abc import ABC
from typing import List
from violations.violation import Violation


class Checker(ABC, ast.NodeVisitor):

    def __init__(self, tree, config):
        self.tree = tree
        self.config = config
        self.violations = []

    def run(self) -> List[Violation]:
        self.visit(self.tree)
        return self.violations 