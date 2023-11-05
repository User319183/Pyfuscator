import ast
import astunparse
import hashlib # Will be used to check if the file has been modified
import random
import string
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

KEY = get_random_bytes(16)  # 16 bytes key for AES-128
IV = get_random_bytes(16)  # 16 bytes initialization vector

def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

cipher = AES.new(KEY, AES.MODE_CFB, IV)  # Reuse the cipher

def encrypt_string(s):
    encrypted = cipher.encrypt(s)
    return b64encode(encrypted).decode()

def decrypt_string(s):
    decrypted = cipher.decrypt(b64decode(s))
    return decrypted.decode()

class Obfuscator(ast.NodeTransformer):
    def __init__(self):
        self.names_map = {}
        self.parent = None

    def visit(self, node):
        old_parent = self.parent
        self.parent = node
        result = super().visit(node)
        self.parent = old_parent
        return result

    def obfuscate(self, code):
        tree = ast.parse(code)
        obfuscated_tree = self.visit(tree)
        return astunparse.unparse(obfuscated_tree)

    def visit_Name(self, node):
        if isinstance(node.ctx, (ast.Load, ast.Store)):
            if node.id not in self.names_map:
                self.names_map[node.id] = random_string()
            node.id = self.names_map[node.id]
        return node

    def visit_FunctionDef(self, node):
        if node.name not in self.names_map:
            self.names_map[node.name] = random_string()
        node.name = self.names_map[node.name]
        self.generic_visit(node)
        return node

    def visit_Str(self, node):
        node.s = encrypt_string(node.s)
        return node

    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)):
            return ast.BinOp(left=ast.Constant(value=node.value), op=ast.Add(), right=ast.Constant(value=0))
        return node

    def visit_JoinedStr(self, node):
        for value in node.values:
            if isinstance(value, ast.FormattedValue) and isinstance(value.value, ast.Name):
                if value.value.id in self.names_map:
                    value.value.id = self.names_map[value.value.id]
        return node

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id in self.names_map:
                node.func.id = self.names_map[node.func.id]
        for arg in node.args:
            if isinstance(arg, ast.Name):
                if arg.id in self.names_map:
                    arg.id = self.names_map[arg.id]
            elif isinstance(arg, ast.JoinedStr):
                for value in arg.values:
                    if isinstance(value, ast.FormattedValue) and isinstance(value.value, ast.Name):
                        if value.value.id in self.names_map:
                            value.value.id = self.names_map[value.value.id]
        return node

class AdvancedObfuscator(Obfuscator):
    def visit_If(self, node):
        new_node = ast.If(test=ast.Constant(value=True), body=[], orelse=[])
        new_node.body.append(node)
        if isinstance(self.parent, (ast.For, ast.While)):
            new_node.body.append(ast.Break())
        return new_node

    def visit_For(self, node):
        # Control flow obfuscation
        new_node = ast.For(target=node.target, iter=node.iter, body=[], orelse=[])
        new_node.body.append(node)
        new_node.body.append(ast.Break())
        return new_node

    def visit_FunctionDef(self, node):
        # Dead code injection
        dead_code = ast.parse("a = 1\nb = 2\na + b").body
        node.body = dead_code + node.body
        return super().visit_FunctionDef(node)
    
    def visit_While(self, node):
        new_node = ast.For(target=ast.Name(id='_', ctx=ast.Store()), iter=ast.Call(func=ast.Name(id='range', ctx=ast.Load()), args=[ast.Constant(value=1000000)], keywords=[]), body=node.body, orelse=[])
        return new_node
    
if __name__ == "__main__":
    obfuscator = AdvancedObfuscator()
    with open('main.py', 'r') as file:
        code = file.read()
    obfuscated_code = obfuscator.obfuscate(code)
    with open('obfuscated_main.py', 'w') as file:
        file.write(obfuscated_code)