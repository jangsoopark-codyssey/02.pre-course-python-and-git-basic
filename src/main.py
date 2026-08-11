# main.py

from common import definitions
from common import dotenv
from common import utils

import application

import argparse
import os
import sys


dotenv.load_dotenv(
    path=os.path.join(
        definitions.project_root,
        'data',
        '.env'
    ),
    override=True
)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Quiz game"
    )

    parser.add_argument(
        '--data-file-path',
        type=str,
        help='Path to the data file'
    )

    parser.add_argument(
        '--data-file-name',
        type=str,
        help='Name of the data file'
    )

    args = parser.parse_args()

    if args.data_file_path:
        os.environ['DATA_FILE_PATH'] = args.data_file_path

    if args.data_file_name:
        os.environ['DATA_FILE_NAME'] = args.data_file_name


def main():
    parse_args()

    state_path = os.path.join(
        definitions.project_root,
        os.getenv('DATA_FILE_PATH'),
        os.getenv('DATA_FILE_NAME')
    )

    configs = utils.load_state(state_path)

    if configs is None:
        return 1

    app_config = configs.get('application', {})
    quizzes = configs.get('quizzes', [])
    score = configs.get(
        'score',
        {
            'last': 0,
            'best': 0,
            'history': []
        }
    )

    app = application.Application(
        name=app_config.get('title'),
        menu=app_config.get('menu'),
        quizzes=quizzes,
        score=score,
        state_path=state_path,
    )

    app.run()

    return 0


if __name__ == "__main__":
    sys.exit(main())