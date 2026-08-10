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

    args = parser.parse_args()

    # Set environment variables based on command-line arguments
    if args.data_file_path:
        os.environ['DATA_FILE_PATH'] = args.data_file_path
    if args.data_file_name:
        os.environ['DATA_FILE_NAME'] = args.data_file_name

    return args


def main():
    args = parse_args()

    state_path = os.path.join(
        definitions.project_root,
        'data',
        os.getenv('DATA_FILE_NAME')
    )

    definitions.initialize(state_path)
    # TODO: Refactoring - with New Branch
    try:
        configs = json.load(
            open(
                state_path, 
                mode='r', encoding='utf-8'
            )
        )
    except json.JSONDecodeError as e:
        print("데이터 파일이 손상되었습니다. 기본 데이터로 복구합니다.")

        definitions.initialize(state_path, force=True)

        configs = json.load(
            open(
                state_path,
                mode='r',
                encoding='utf-8'
            )
        )
    
    app_config = configs.get('application', {})
    quizzes = configs.get('quizzes', [])
    best_score = configs.get('best_score', 0)

    
    # Initialize the application with the loaded configurations
    app = application.Application(
        name=app_config.get('title'),
        menu=app_config.get('menu'),
        quizzes=quizzes,
        best_score=best_score,
        state_path=state_path,

    )
    
    # Run the application
    app.run()

    return 0


if __name__ == "__main__":
    sys.exit(main())
