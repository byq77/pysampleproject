from importlib.resources import files

import json5 as json

from . import VERSION_WITH_COPYRIGHT
from .sample import greet


def main():
    CONFIG = json.loads(files("sample").joinpath("config.json5").read_text())
    print(VERSION_WITH_COPYRIGHT)
    greet(CONFIG["name"])


if __name__ == "__main__":
    main()
