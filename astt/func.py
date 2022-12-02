import ast

from rich import print as rprint


class visit_imports(ast.NodeVisitor):

    def __init__(self):
        self.imports = []

    def visit_Import(self, node: ast.Import):
        self.imports.append(node.names[0].name)

        return super().generic_visit(node)


    def visit_ImportFrom(self, node: ast.ImportFrom):
        self.imports.append(node.module)

        for module in node.names:
            self.imports.append(module.name)

        return super().generic_visit(node)


def check(node: ast.AST, config: dict, filename: str, imports: list) -> None:
    if not hasattr(node, 'lineno'):
        return False

    for rule in config.config:
        func = config.config[rule]['rule']
        warn = config.config[rule]['message']
        node_type = config.config[rule]['node']
        line = node.lineno

        if isinstance(node, node_type) and func(node, imports):
            rprint(f'{filename}:{line}: [red]{rule}[/] {warn}')

    return None
