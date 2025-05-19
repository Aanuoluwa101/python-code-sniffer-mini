
from config import checks
import ast 


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