from common import definitions
from common import dotenv

import application

import argparse
import json
import sys
import os


# Load environment variables from .env file
dotenv.load_dotenv(path=os.path.join(definitions.project_root, 'data', ".env"), override=True)


def parse_args():
    
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument('--data-file-path', type=str, help='Path to the data file')
    parser.add_argument('--data-file-name', type=str, help='Name of the data file')
    parser.add_argument('--static-file-name', type=str, help='Name of the static file')

    args = parser.parse_args()

    # Set environment variables based on command-line arguments
    if args.data_file_path:
        os.environ['DATA_FILE_PATH'] = args.data_file_path
    if args.data_file_name:
        os.environ['DATA_FILE_NAME'] = args.data_file_name
    if args.static_file_name:
        os.environ['STATIC_FILE_NAME'] = args.static_file_name

    return args


def main():
    args = parse_args()
    
    configs = json.load(
        open(
            os.path.join(definitions.project_root, 'data', os.getenv('STATIC_FILE_NAME')), 
            mode='r', encoding='utf-8'
        )
    )['application']

    app = application.Application(
        name=configs.get('title'),
        menu=configs.get('menu')
    )

    
    app.run()
    # print(definitions.project_root)
    # print(os.getenv('DATA_FILE_PATH'))
    # print(os.getenv('DATA_FILE_NAME'))

    return 0


if __name__ == "__main__":
    sys.exit(main())
