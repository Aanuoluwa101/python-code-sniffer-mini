import ast


def fetch_tree(filepath):
    try:
        with open(filepath) as f:
            source_code = f.read() 
            return ast.parse(source_code) 
    except FileNotFoundError:
        raise Exception(f"Can't open {filepath}. Make sure the path exists and is correct")
    except SyntaxError as e:
        raise Exception(f"Invalid python file: {e}")
    except Exception as e:
        raise Exception(f"Could not fetch tree: {e}")
