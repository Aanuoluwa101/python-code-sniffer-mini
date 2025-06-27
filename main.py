from sniffer import Sniffer
import argparse
from utils import load_config, fetch_tree



def main():
    try:
        config = load_config()

        parser = argparse.ArgumentParser(description="Static analysis sniffer for Python code.")
        parser.add_argument('--file', type=str, required=True, help='Path to the Python file to analyze')    
        args = parser.parse_args()

        tree = fetch_tree(args.file)

        sniffer = Sniffer(tree, config)
        sniffer.sniff()
    except Exception as e:
        print(f"ERROR RUNNING SNIIFER: {e}")


if __name__ == "__main__":
    main()