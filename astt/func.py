import ast


def check(node: ast.AST, config: dict, filename: str) -> None:
    if not hasattr(node, 'lineno'):
        return False

    for rule in config.config:
        func = config.config[rule]['rule']
        warn = config.config[rule]['message']
        node_type = config.config[rule]['node']
        start = node.lineno
        end = node.end_lineno
        row = node.col_offset

        if isinstance(node, node_type) and func(node):
            print(f'[{rule}] {warn} {filename}@{start}-{end}:{row}')

    return None
