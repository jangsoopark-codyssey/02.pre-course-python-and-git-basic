from . import constants

import json
import os


project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def initialize(path):
    
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(constants.DEFAULT_DATA, f, ensure_ascii=False, indent=4)
    