
import ast 
from violations import Violation
from checkers import CheckerRunner


class Sniffer:     
    def __init__(self, tree: ast.AST, config: dict):
        self.tree = tree
        self.config = config
               
    def sniff(self):
        try:
            runner = CheckerRunner(self.tree, self.config)
            runner.run()
            violations = runner.violations
            if not all([issubclass(violation.__class__, Violation) for violation in violations]):
                    raise ValueError("checker.run must return a list of Violations")
            
            if not violations:
                print("\033[92mAll looks good!\033[0m")
            else: 
                print(f"\033[91m{len(violations)} violation(s)\033[0m")
                for violation in violations:
                    print(violation)
        except Exception as e:
            raise Exception(f"ERROR RUNNING SNIFFER: {e}")