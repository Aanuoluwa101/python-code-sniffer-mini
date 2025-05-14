from checkers.function_length_checker import FunctionLengthChecker

class CodeSniffer:
    # the file we're sniffing
    # config file which will be passed to checkers 

    pass 

    def __init__(self):
        self.checkers = [
            FunctionLengthChecker()
        ]