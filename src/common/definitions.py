from . import constants

import json
import os


project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
max_num_choices = 4


def initialize(path):
    if os.path.exists(path):
        return

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(
            constants.DEFAULT_DATA,
            f,
            ensure_ascii=False,
            indent=4
        )