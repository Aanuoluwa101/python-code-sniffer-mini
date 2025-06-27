
import ast 
from violations import Violation
from config import registered_checkers


class Sniffer:     
    def __init__(self, tree: ast.AST, rules: dict):
        self.tree = tree
        self.rules = rules
               
    def sniff(self):
        try:
            all_violations = []
            for checker_class in registered_checkers:
                checker = checker_class(self.tree, self.rules)
                checker.run()
                violations = checker.violations
                if not all([issubclass(violation.__class__, Violation) for violation in violations]):
                    raise ValueError("checker.run must return a list of Violations")
                all_violations.extend(violations)
            
            if not all_violations:
                print("\033[92mAll looks good!\033[0m")
            else: 
                print(f"\033[91m{len(all_violations)} violation(s)\033[0m")
                for violation in all_violations:
                    print(violation)
        except Exception as e:
            raise Exception(f"ERROR RUNNING SNIFFER: {e}")