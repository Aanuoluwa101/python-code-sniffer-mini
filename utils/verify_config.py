from checkers.checker import Checker
from config import checks

def verify_config(self):
    for index, check in enumerate(checks):
        name, checker, config = check.get("name"), check.get("checker"), check.get("config")
        if not name or not isinstance(name, str):
            raise ValueError(f"Invalid Config file (config {index + 1}): name must be a valid string")

        if not checker or not isinstance(checker, Checker):
            raise ValueError(f"Invalid Config file (config {index + 1}): a checker of type Checker must be provided")
        
        if config and not isinstance(config, dict):
            raise ValueError(f"Invalid Config file (config {index + 1}): config must be a dictionary")