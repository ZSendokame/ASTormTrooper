import ast


class visit_imports(ast.NodeVisitor):

    def __init__(self):
        self.imports = []

    def visit_Import(self, node: ast.Import):
        self.imports.append(node.names[0].name)

        return super().generic_visit(node)


def check(node: ast.AST, config: dict, filename: str, imports: list) -> None:
    if not hasattr(node, 'lineno'):
        return False

    for rule in config.config:
        func = config.config[rule]['rule']
        warn = config.config[rule]['message']
        node_type = config.config[rule]['node']
        start = node.lineno
        end = node.end_lineno
        row = node.col_offset

        if isinstance(node, node_type) and func(node, imports):
            print(f'[{rule}] {warn} {filename}@{start}-{end}:{row}')

    return None
