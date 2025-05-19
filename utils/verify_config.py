from checkers.checker import Checker
from config import checks

def verify_config():
    for index, check in enumerate(list(checks.values())):
        checker, config = check.get("checker"), check.get("config")
        if not checker or not issubclass(checker, Checker):
            raise ValueError(f"Invalid Config file (config {index + 1}): a checker of type Checker must be provided")
        
        if config and not isinstance(config, dict):
            raise ValueError(f"Invalid Config file (config {index + 1}): config must be a dictionary")