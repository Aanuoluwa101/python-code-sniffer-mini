import ast
from abc import ABC, abstractmethod
import json
from typing import List
from violations.violation import Violation


class  Checker(ABC, ast.NodeVisitor):
    default_config_file = "config.json"

    def __init__(self, config_file: str = None):
        if config_file:
            if not config_file.endswith(".json"):
                raise ValueError("Config must be a json file")
        else:
            config_file = self.default_config_file
        
        with open(config_file) as file:
            self.config = json.load(file)
            
        self.violations = []

    # this run method is bad
    @abstractmethod
    def run(self, source_code) -> List[Violation]:
        pass