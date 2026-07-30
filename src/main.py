from common import definitions
from common import dotenv

import sys
import os

# Load environment variables from .env file
dotenv.load_dotenv(path=os.path.join(definitions.project_root, 'data', ".env"), override=True)


def main():
    print(definitions.project_root)
    print(os.getenv('DATA_FILE_PATH'))
    print(os.getenv('DATA_FILE_NAME'))


if __name__ == "__main__":
    sys.exit(main())
