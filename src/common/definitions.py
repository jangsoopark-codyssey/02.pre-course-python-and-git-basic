from . import constants

import json
import os


project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
max_num_choices = 4


def initialize(path, force=False):
    if os.path.exists(path) and not force:
        return True

    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(
                constants.DEFAULT_DATA,
                f,
                ensure_ascii=False,
                indent=4
            )

    except OSError as e:
        print(f"데이터 파일을 초기화하는 중 오류가 발생했습니다: {e}")
        return False

    return True