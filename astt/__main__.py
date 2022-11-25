import ast
import os

import arguing

from . import func


def main():
    config = arguing.set('-c', default='lint', help='Python file with rules.')
    exclude = arguing.set('-e', help='Files to exclude from linting.')

    if not os.path.exists(config + '.py'):
        exit(f'[-] {config} not found, please create one and configure it.')

    lint = __import__(config)
    remove = exclude.split(',')
    directory = [
        file
        for file in os.listdir()
        if os.path.isfile(file)
        and file not in remove
        and file.endswith('.py')
    ]

    for file in directory:
        file = open(file, 'r')
        parsed = ast.parse(file.read())

        for node in ast.walk(parsed):
            func.check(node=node, config=lint, filename=file.name)

        file.close()


if __name__ == '__main__':
    main()
