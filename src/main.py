from common import definitions
from common import dotenv

import argparse
import sys
import os

# Load environment variables from .env file
dotenv.load_dotenv(path=os.path.join(definitions.project_root, 'data', ".env"), override=True)


def parse_args():
    
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument('--data-file-path', type=str, help='Path to the data file')
    parser.add_argument('--data-file-name', type=str, help='Name of the data file')

    args = parser.parse_args()

    # Set environment variables based on command-line arguments
    if args.data_file_path:
        os.environ['DATA_FILE_PATH'] = args.data_file_path
    if args.data_file_name:
        os.environ['DATA_FILE_NAME'] = args.data_file_name

    return args


def main():
    args = parse_args()

    print(definitions.project_root)
    print(os.getenv('DATA_FILE_PATH'))
    print(os.getenv('DATA_FILE_NAME'))

    return 0


if __name__ == "__main__":
    sys.exit(main())
