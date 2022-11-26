import ast
import os

import arguing

from . import func


def main():
    start = arguing.set('-a', default='.', help='Starting directory to scan.')
    config = arguing.set('-c', default='lint', help='Python file with rules.')
    exclude = arguing.set('-e', help='Files to exclude from linting.')
    lint = __import__(config)
    exclude = exclude.split(',')

    exclude.append(config)

    for root, directory, files in os.walk(start):
        for file in files:
            if file not in exclude and file.endswith('py'):
                file = open(f'{root}\{file}', 'r')
                parsed = ast.parse(file.read())

                for node in ast.walk(parsed):
                    func.check(node=node, config=lint, filename=file.name)

                file.close()


if __name__ == '__main__':
    main()
