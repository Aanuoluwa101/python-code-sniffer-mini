import ast
from abc import ABC, abstractmethod


class Checker(ABC, ast.NodeVisitor):
    def __init__(self, tree: ast.AST, rules: dict):
        self.tree = tree
        self.rules = rules
        self.violations = []

    def run(self):
        self.visit(self.tree)