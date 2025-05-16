
from config import checks
import ast 
from checkers.checker import Checker

class Sniffer:     
    def __init__(self, source_file):
        self.verify_config()
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
        
    def verify_config(self):
        for index, check in enumerate(checks):
            name, checker, config = check.get("name"), check.get("checker"), check.get("config")
            if not name or not isinstance(name, str):
                raise ValueError(f"Invalid Config file (config {index + 1}): name must be a valid string")

            if not checker or not isinstance(checker, Checker):
                 raise ValueError(f"Invalid Config file (config {index + 1}): a checker of type Checker must be provided")
            
            if config and not isinstance(config, dict):
                raise ValueError(f"Invalid Config file (config {index + 1}): config must be a dictionary")

               
    def sniff(self):
        try:
            all_violations = []
            for check in checks:
                checker, config = check["checker"], checker["config"]
                checker = checker(self.tree, config)
                violations = checker.run()
                all_violations.extend(violations)
            
            if not violations:
                print("All looks good!")
            else: 
                print(f"{len(all_violations)} violations!")
                for violation in all_violations:
                    print(violation)
        except Exception as e:
            raise Exception(f"ERROR RUNNING SNIFFER: {e}")