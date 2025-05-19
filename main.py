from sniffer import Sniffer
import argparse
from utils.verify_config import verify_config


def main():
    verify_config()
    
    parser = argparse.ArgumentParser(description="Static analysis sniffer for Python code.")
    parser.add_argument('--file', type=str, required=True, help='Path to the Python file to analyze')    
    args = parser.parse_args()

    sniffer = Sniffer(args.file)
    sniffer.sniff()


if __name__ == "__main__":
    main()