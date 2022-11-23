import ast
import os

import arguing


def main():
    config = arguing.set('-c', default='lint', help='Python file with rules.')
    exclude = arguing.set('-e', help='Files to exclude from linting.')

    if not os.path.exists(config + '.py'):
        exit(f'[-] {config} not found, please create one and configure it.')

    lint = __import__(config)
    exclude = exclude.split(',')
    directory = [
        file
        for file in os.listdir()
        if os.path.isfile(file)
        and file not in exclude
        and file.endswith('.py')
    ]

    for file in directory:
        file = open(file, 'r')
        parsed = ast.parse(file.read())

        for node in ast.iter_child_nodes(parsed):
            for rule in lint.config:
                warn = lint.config[rule]['message']
                func = lint.config[rule]['rule']
                node_type = lint.config[rule]['node']
                line = node.lineno
                row = node.col_offset

                if isinstance(node, node_type) and func(node):
                    print(f'[{rule}] {warn} {file.name}@{line}:{row}')

        file.close()


if __name__ == '__main__':
    main()
