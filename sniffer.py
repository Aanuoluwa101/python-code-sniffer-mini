
from config import checks
import ast 
from violations import Violation


class Sniffer:     
    def __init__(self, source_file):
        try:
            with open(source_file) as f:
                source_code = f.read() 
            
            self.tree = ast.parse(source_code)
        except FileNotFoundError:
            raise Exception(f"Can't open {source_file}. Make sure the path exists and is correct")
        except SyntaxError as e:
            raise Exception(f"Invalid python file: {e}")
        except Exception as e:
            raise e
               
    def sniff(self):
        try:
            all_violations = []
            for check in checks.values():
                checker, config = check["checker"], check["config"]
                checker = checker(self.tree, config)
                violations = checker.run()
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