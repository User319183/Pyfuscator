"""
This obfuscator is protected by the MIT License. Please read the license before using this obfuscator.
This is my custom Python obfuscator. It's not the best, but it's free and open source. I'm not responsible for any damage caused by this program. Use at your own risk.
Created by User319183
"""

import random
import string
import json
import ast
import astunparse
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

KEY = get_random_bytes(32)  # 32 bytes key for AES-256.
RSA_KEY = RSA.generate(2048)  # 2048-bit RSA key
RSA_CIPHER = PKCS1_OAEP.new(RSA_KEY)

def random_string(length=100):
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def encrypt_with_aes_and_rsa(plain_text):
    IV = get_random_bytes(16)  # 16 bytes initialization vector
    cipher_aes = AES.new(KEY, AES.MODE_CFB, IV)  # AES cipher
    cipher_text_aes = cipher_aes.encrypt(plain_text)
    cipher_text_rsa = RSA_CIPHER.encrypt(cipher_text_aes)  # RSA cipher
    return cipher_text_rsa

cipher = AES.new(KEY, AES.MODE_CFB, get_random_bytes(16))

def encrypt_string(s):
    encrypted = cipher.encrypt(s)
    return b64encode(encrypted).decode()

def decrypt_string(s):
    decrypted = cipher.decrypt(b64decode(s))
    return decrypted.decode()

class Obfuscator(ast.NodeTransformer):
    """
    The base class for the obfuscator. This class contains the basic obfuscation techniques.
    """
    def __init__(self):
        self.names_map = {}
        self.strings_table = []
        self.char_map = {char: i for i, char in enumerate(string.printable)}
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
        obfuscated_code = astunparse.unparse(obfuscated_tree)
        char_map_code = f"char_map = {self.char_map}\n"
        strings_table_code = f"strings_table = {self.strings_table}\n"
        info = { # New feature
        "Obfuscator": {
            "Created_By": {
                "User319183": "Free | Open Source Version",
                "Should I create a premium version?": "lol probably not b/c I'm lazy",
                "Join the Discord if your a kool kid": "https://discord.gg/KHJjX3y2B4",
            },
            "Features": {
                "Random_String_Generation": 'true', # Updated feature
                "AES_and_RSA_Encryption": 'true', # Updated feature
                "String_Encryption": 'true', # Updated feature
                "String_Decryption": 'true', # Updated feature
                "Code_Obfuscation": 'true', # Updated feature
                "Name_Obfuscation": 'true', # Updated feature
                "Function_Name_Obfuscation": 'true',
                "String_Obfuscation": 'true', # Updated feature
                "Constant_Obfuscation": 'true', # Updated feature
                "Call_Obfuscation": 'true', # Updated feature
                "Advanced_Obfuscation": {
                    "Code_Flattening": 'true', # Updated feature (I think)
                    "Proprietary_Logic_Insertion": 'true', # New feature
                    "Safeguard_Insertion": 'true', # New feature
                    "Dead_Code_Insertion": 'true', # Updated feature
                    "Control_Flow_Flattening": 'true',  # New feature
                    "Code_Substitution": 'true',  # New feature
                    "Dummy_Code_Insertion": 'true',  # New feature
                    "Variable_Renaming": 'true',  # New feature
                }
            }
        }
    }
        version_info = "credits = " + json.dumps(info, indent=4) + "\n"
        return version_info + char_map_code + strings_table_code + obfuscated_code
    
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
        encrypted_string = encrypt_with_aes_and_rsa(node.s)
        index = len(self.strings_table)
        self.strings_table.append(encrypted_string)
        node.s = f"strings_table[{index}]"
        return node

    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)):
            offset = random.randint(-100, 100)  # Generate a random offset
            node.value = node.value + offset - offset  # Obfuscate the number by adding and subtracting the offset
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
    """
    This class contains advanced obfuscation techniques.
    Including, but not limited to: 
    - Code flattening
    - Proprietary logic insertion
    - Safeguard insertion
    - Dead code insertion
    - Control flow flattening
    - Code substitution
    - Dummy code insertion
    - Variable renaming
    """
    
    def flatten(self, node):
        shuffled_body = list(node.body)
        random.shuffle(shuffled_body)
        
        control_var = random_string()
        ranges_table = [[i, i+1] for i in range(len(node.body))]

        for i, body_node in enumerate(shuffled_body):
            if_node = ast.If(
                test=ast.Compare(
                    left=ast.Name(id=control_var, ctx=ast.Load()),
                    ops=[ast.GtE(), ast.Lt()],
                    comparators=[ast.Constant(value=ranges_table[i][0]), ast.Constant(value=ranges_table[i][1])]
                ),
                body=[body_node, ast.Assign(
                    targets=[ast.Name(id=control_var, ctx=ast.Store())],
                    value=ast.BinOp(left=ast.Name(id=control_var, ctx=ast.Load()), op=ast.Add(), right=ast.Constant(value=1))
                )],
                orelse=[]
            )
            shuffled_body[i] = if_node

        node.body = [
            ast.Assign(
                targets=[ast.Name(id=control_var, ctx=ast.Store())],
                value=ast.Constant(value=0)
            ),
            ast.While(
                test=ast.Constant(value=True),
                body=shuffled_body,
                orelse=[]
            )
        ]

        return node

    def proprietary_logic(self, node):
        print_node = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Str(s=node.name)], keywords=[]))
        node.body.insert(0, print_node)
        return node
    def safeguard(self, node):
        class ReplaceIntegers(ast.NodeTransformer):
            def visit_Constant(self, node):
                if isinstance(node.value, int):
                    return ast.BinOp(left=ast.Constant(value=node.value + 1), op=ast.Sub(), right=ast.Constant(value=1))
                return node

        ReplaceIntegers().visit(node)
        return node
    
    def generate_dead_code(self):
        dead_code_type = random.choice(['noop_loop', 'meaningless_calc', 'unused_var'])
        if dead_code_type == 'noop_loop':
            return ast.For(
                target=ast.Name(id='_', ctx=ast.Store()),
                iter=ast.Call(func=ast.Name(id='range', ctx=ast.Load()), args=[ast.Constant(value=random.randint(1, 10))], keywords=[]),
                body=[ast.Pass()],
                orelse=[]
            )
        elif dead_code_type == 'meaningless_calc':
            return ast.Expr(
                value=ast.BinOp(
                    left=ast.Constant(value=random.randint(1, 10)),
                    op=ast.Add(),
                    right=ast.Constant(value=random.randint(1, 10))
                )
            )
        elif dead_code_type == 'unused_var':
            return ast.Assign(
                targets=[ast.Name(id=random_string(), ctx=ast.Store())],
                value=ast.Constant(value=random.randint(1, 10))
            )

    def visit_FunctionDef(self, node):
        node = self.flatten(node)
        node = self.proprietary_logic(node)
        node = self.safeguard(node)
        dead_code = self.generate_dead_code()
        node.body.insert(random.randint(0, len(node.body)), dead_code)
        return super().visit_FunctionDef(node)
    
    def visit_Module(self, node):
        for _ in range(random.randint(1, 3)): # Insert 1-3 dead code snippets
            dead_code = self.generate_dead_code()
            node.body.insert(random.randint(0, len(node.body)), dead_code)
        self.generic_visit(node)
        return node

    def visit_While(self, node):
        new_node = ast.For(target=ast.Name(id='_', ctx=ast.Store()), iter=ast.Call(func=ast.Name(id='range', ctx=ast.Load()), args=[ast.Constant(value=1000000)], keywords=[]), body=node.body, orelse=[])
        return new_node
    
class Supremebfuscator(AdvancedObfuscator):
    """
    This class contains the most advanced obfuscation techniques.
    Including, but not limited to:
    - Opaque predicates
    - Encrypted strings
    - Control flow flattening    
    """
    def __init__(self):
        super().__init__()
        self.opaque_predicates_table = []
        self.encrypted_strings_table = []
        
    def control_flow_flattening(self, code):
        # Parse the code into an AST
        tree = ast.parse(code)

        # Create a NodeTransformer to flatten the control flow
        class ControlFlowFlattener(ast.NodeTransformer):
            def visit_If(self, node):
                # Generate a random variable name for the control variable
                control_var = random_string()

                # Create a list of the bodies of the if and else branches
                bodies = [node.body, node.orelse]
                
                random.shuffle(bodies)

                # Create a switch statement with a case for each body
                switch_statement = ast.Switch(
                    test=ast.Name(id=control_var, ctx=ast.Load()),
                    body=[ast.case(index, body) for index, body in enumerate(bodies)]
                )

                # Create a loop that iterates over the cases in the switch statement
                loop = ast.For(
                    target=ast.Name(id=control_var, ctx=ast.Store()),
                    iter=ast.Call(func=ast.Name(id='range', ctx=ast.Load()), args=[ast.Constant(value=len(bodies))], keywords=[]),
                    body=[switch_statement],
                    orelse=[]
                )
                return loop

        # Apply the NodeTransformer to the AST
        ControlFlowFlattener().visit(tree)

        # Unparse the AST back into code
        return astunparse.unparse(tree)

    def opaque_predicate(self):
        # Generate a condition that always evaluates to true
        condition = ast.Compare(
            left=ast.BinOp(
                left=ast.Constant(value=random.randint(1, 10000)),
                op=ast.Add(),
                right=ast.Constant(value=random.randint(1, 10000))
            ),
            ops=[ast.Eq()],
            comparators=[ast.BinOp(
                left=ast.Constant(value=random.randint(1, 10000)),
                op=ast.Add(),
                right=ast.Constant(value=random.randint(1, 10000))
            )]
        )
        self.opaque_predicates_table.append(condition)
        return f"opaque_predicates_table[{len(self.opaque_predicates_table) - 1}]"

    def visit_If(self, node):
        node.test = ast.BoolOp(op=ast.And(), values=[node.test, ast.Name(id=self.opaque_predicate(), ctx=ast.Load())])
        return node

    def visit_While(self, node):
        node.test = ast.BoolOp(op=ast.And(), values=[node.test, ast.Name(id=self.opaque_predicate(), ctx=ast.Load())])
        return node

    def visit_Str(self, node):
        encrypted_string = encrypt_with_aes_and_rsa(node.s.encode()).decode()
        index = len(self.encrypted_strings_table)
        self.encrypted_strings_table.append(encrypted_string)
        node.s = f"decrypt_string(encrypted_strings_table[{index}])"
        return node

    def obfuscate(self, code):
        # Obfuscate the code using the base obfuscator, then obfuscate the obfuscated code using the advanced obfuscator, then obfuscate the obfuscated obfuscated code using the supremebfuscator
        obfuscated_code = super().obfuscate(code)
        opaque_predicates_table_code = "opaque_predicates_table = ["
        for node in self.opaque_predicates_table:
            opaque_predicates_table_code += encrypt_with_aes_and_rsa(ast.dump(node).encode()).decode() + ", "
        opaque_predicates_table_code = opaque_predicates_table_code.rstrip(", ") + "]\n"
        return opaque_predicates_table_code + obfuscated_code

if __name__ == "__main__":
    obfuscator = Supremebfuscator()
    with open('main.py', 'r') as file:
        code = file.read()
    obfuscated_code = obfuscator.obfuscate(code)
    with open('obfuscated_main.py', 'w', encoding='utf-8') as file:
        file.write(obfuscated_code)
