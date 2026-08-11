# common/utils.py

from common import constants

import json
import os


def initialize(path, force=False):
    if os.path.exists(path) and not force:
        return True

    try:
        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )

        with open(
            path,
            'w',
            encoding='utf-8'
        ) as f:
            json.dump(
                constants.DEFAULT_DATA,
                f,
                ensure_ascii=False,
                indent=4
            )

    except OSError as e:
        print(
            f"데이터 파일을 초기화하는 중 오류가 발생했습니다: {e}"
        )
        return False

    return True


def load_json_file(path):
    with open(
        path,
        'r',
        encoding='utf-8'
    ) as f:
        return json.load(f)


def load_state(path):
    # Initialize the data file if it does not exist
    if not initialize(path):
        return None

    try:
        return load_json_file(path)

    except json.JSONDecodeError:
        print(
            "데이터 파일이 손상되었습니다. "
            "기본 데이터로 복구합니다."
        )

        if not initialize(
            path,
            force=True
        ):
            return None

    except OSError as e:
        print(
            f"데이터 파일을 읽는 중 오류가 발생했습니다: {e}"
        )
        return None

    # Reload the restored data file
    try:
        return load_json_file(path)

    except (json.JSONDecodeError, OSError) as e:
        print(
            f"복구된 데이터 파일을 읽는 중 오류가 발생했습니다: {e}"
        )
        return None


def input_text(prompt):
    while True:
        try:
            value = input(prompt).strip()

            if not value:
                print("값을 입력해주세요.")
                continue

            return value

        except KeyboardInterrupt:
            print("\nCtrl+C 입력은 사용할 수 없습니다.")

        except EOFError:
            print("\n입력이 종료되었습니다. 다시 입력해주세요.")


def input_number(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt).strip())

            if value < min_value or value > max_value:
                print(
                    f"잘못된 입력입니다. "
                    f"{min_value}~{max_value} 사이의 숫자를 입력해주세요."
                )
                continue

            return value

        except ValueError:
            print(
                f"잘못된 입력입니다. "
                f"{min_value}~{max_value} 사이의 숫자를 입력해주세요."
            )

        except KeyboardInterrupt:
            print("\nCtrl+C 입력은 사용할 수 없습니다. 다시 입력해주세요.")

        except EOFError:
            print("\n입력이 종료되었습니다. 다시 입력해주세요.")


def save_json_file(path, data):
    try:
        with open(
            path,
            'w',
            encoding='utf-8'
        ) as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )

    except OSError as e:
        print(
            f"데이터 파일을 저장하는 중 오류가 발생했습니다: {e}"
        )
        return False

    return True
