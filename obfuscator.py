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
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import multiprocessing

KEY = get_random_bytes(32)
RSA_KEY = RSA.generate(2048)
RSA_CIPHER = PKCS1_OAEP.new(RSA_KEY)

funny_messages = [
    "User319183 was here!",
    "This code was obfuscated by User319183's Python Obfuscator",
    "This code was obfuscated by User319183's Python Obfuscator. Join the Discord if your a kool kid: https://discord.gg/KHJjX3y2B4",
    "https://e-z.bio/hot",
    "Void Gen on top??!!?!?!?!?!?",
    "Another day, another victory for the OGs",
    "sacrifice loves skidding",
]

random_variables = [
    "we_suck_poo",
    "eat_it_pls",
    "OH_YES_DADDY",
    "void_gen_do_be_super_smexy",
    "i_love_the_person_reading_this",
    "edit_kinda_stinks",
    "poopiesucker3145",
    "king_jun_umu",
    "if_you_put_a_buck_in_my_cup_i_will_suck_you_off",
    "pooron",
    "school_is_for_losers",
]


def random_string(length=500):
    ascii_and_digits = string.ascii_letters
    spanish_chars = "áéíóúñÁÉÍÓÚÑ"
    french_chars = "àâéèêëîïôùûçÀÂÉÈÊËÎÏÔÙÛÇ"
    unknown_chars = "ÿþÿþÿþÿþÿþÿþÿþÿþÿþÿþÿþÿþÿþÿþ"
    chinese_chars = "你好我是User319183我喜欢吃屎"
    return ''.join(random.choices(ascii_and_digits + spanish_chars + french_chars + unknown_chars + chinese_chars, k=length))


def encrypt_with_aes_and_rsa(plain_text):
    IV = get_random_bytes(16)
    cipher_aes = AES.new(KEY, AES.MODE_CFB, IV)
    # Convert the string to bytes before encryption
    cipher_text_aes = cipher_aes.encrypt(plain_text.encode())
    cipher_text_rsa = RSA_CIPHER.encrypt(cipher_text_aes)  # RSA cipher

    return base64.b64encode(cipher_text_rsa).decode()


cipher = AES.new(KEY, AES.MODE_CFB, get_random_bytes(16))

def encrypt_string(s):
    encrypted = cipher.encrypt(s)
    return b64encode(encrypted).decode()

def decrypt_string(s):
    decrypted = cipher.decrypt(b64decode(s))
    return decrypted.decode()

class Obfuscator(ast.NodeTransformer):
    def __init__(self, key=None):
        self.names_map = {}
        self.strings_table = []
        self.char_map = {char: i for i, char in enumerate(string.printable)}
        self.parent = None
        self.key = key if key else get_random_bytes(32)
        self.used_names = set() # Used to prevent name collisions

    def visit(self, node):
        old_parent = self.parent
        self.parent = node
        result = super().visit(node)
        self.parent = old_parent
        return result

    def obfuscate(self, code):
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            print(f"Failed to parse code: {e}")
            return code
        obfuscated_tree = self.visit(tree)
        obfuscated_code = astunparse.unparse(obfuscated_tree)
        char_map_code = f"char_map = {self.char_map}\n"
        strings_table_code = f"strings_table = {self.strings_table}\n"
        info = {
        "Obfuscator": {
            "Created_By": {
                "User319183": "Free | Open Source Version",
                "Should I create a premium version?": "lol probably not b/c I'm lazy",
                "Join the Discord if your a kool kid": "https://discord.gg/KHJjX3y2B4",
            },
            "Features": {
                "Random_String_Generation": 'true',
                "AES_and_RSA_Encryption": 'true',
                "String_Encryption": 'true',
                "String_Decryption": 'true',
                "Code_Obfuscation": 'true',
                "Name_Obfuscation": 'true',
                "Function_Name_Obfuscation": 'true',
                "String_Obfuscation": 'true',
                "Constant_Obfuscation": 'true',
                "Call_Obfuscation": 'true',
                "Advanced_Obfuscation": {
                    "Code_Flattening": 'true',
                    "Proprietary_Logic_Insertion": 'true',
                    "Safeguard_Insertion": 'true',
                    "Dead_Code_Insertion": 'true',
                    "Code_Substitution": 'true',
                    "Dummy_Code_Insertion": 'true',
                    "Variable_Renaming": 'true',
                },
                
                "Supremebfuscator": {
                    "Opaque_Predicates": 'true', # New feature
                    "Encrypted_Strings": 'true', # New feature
                    "Control_Flow_Flattening": 'true', # New feature
                    "Parallel_Obfuscation": 'true', # New feature
                }
            }
        }
    }
        
        version_info = "credits = " + json.dumps(info, indent=4) + "\n"
        lines = obfuscated_code.split('\n')
        for i, message in enumerate(funny_messages):
            random_index = random.randint(0, len(lines))
            # Insert a funny message at a random line. The funny message is a comment but we will work on making it a valid statement later.
            lines.insert(random_index, f'# {random.choice(random_variables)} = "{message}"')
        obfuscated_code = '\n'.join(lines)
        
        return version_info + char_map_code + strings_table_code + obfuscated_code

    def visit_Name(self, node):
        if isinstance(node.ctx, (ast.Load, ast.Store)):
            if node.id not in self.names_map:
                new_name = self.generate_unique_name()
                self.names_map[node.id] = new_name
            node.id = self.names_map.get(node.id, node.id)
        return node

    def visit_FunctionDef(self, node):
        obfuscated_name = ''.join(random.choices(string.ascii_letters, k=10))
        # Add the original name and the obfuscated name to the names_map dictionary
        self.names_map[node.name] = obfuscated_name
        node.name = obfuscated_name
        return self.generic_visit(node)

    def generate_unique_name(self):
        while True:
            name = random_string()
            if name not in self.used_names:
                self.used_names.add(name)
                return name
            
    def visit_Str(self, node):
        encrypted_string = encrypt_with_aes_and_rsa(node.s)
        index = len(self.strings_table)
        self.strings_table.append(encrypted_string)
        node.s = f"decrypt_string(strings_table[{index}])" # Decrypt the string before returning it
        return node

    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)):
            offset = random.randint(1, 99999)
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
                iter=ast.Call(func=ast.Name(id='range', ctx=ast.Load()), args=[ast.Constant(value=random.randint(1, 10000))], keywords=[]),
                body=[ast.Pass()],
                orelse=[]
            )
        elif dead_code_type == 'meaningless_calc':
            return ast.Expr(
                value=ast.BinOp(
                    left=ast.Constant(value=random.randint(1, 99999)),
                    op=ast.Add(),
                    right=ast.Constant(value=random.randint(1, 99999)),
                )
            )
        elif dead_code_type == 'unused_var':
            return ast.Assign(
                targets=[ast.Name(id=random_string(), ctx=ast.Store())],
                value=ast.Constant(value=random.randint(1, 99999))
                    
            )

    def visit_FunctionDef(self, node):
        node = self.flatten(node)
        node = self.proprietary_logic(node)
        node = self.safeguard(node)
        dead_code = self.generate_dead_code()
        node.body.insert(random.randint(0, len(node.body)), dead_code)
        return super().visit_FunctionDef(node)
    
    def visit_Module(self, node):
        for _ in range(random.randint(1, 100)):
            node.body.insert(random.randint(0, len(node.body)), self.generate_dead_code())
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
    - Code flattening
    - Proprietary logic insertion
    - Safeguard insertion
    - Dead code insertion
    - Code substitution
    - Dummy code insertion
    - Variable renaming
    - Parallel obfuscation
    """
    def __init__(self):
        super().__init__()
        self.opaque_predicates_table = []
        self.encrypted_strings_table = []
        
        
    class ControlFlowFlattener(ast.NodeTransformer):
        def visit_If(self, node):
            # Generate a random variable name for the control variable
            control_var = random_string()

            # Create a list of the bodies of the if and else branches
            bodies = [node.body]
            if node.orelse:
                bodies.append(node.orelse)

            random.shuffle(bodies)

            # Create a list of if-elif statements
            if_elif_statements = []
            for index, body in enumerate(bodies):
                if index == 0:
                    if_elif_statements.append(ast.If(test=ast.Compare(left=ast.Name(id=control_var, ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(value=index)]), body=body, orelse=[]))
                else:
                    if_elif_statements[-1].orelse.append(ast.If(test=ast.Compare(left=ast.Name(id=control_var, ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(value=index)]), body=body, orelse=[]))

            return if_elif_statements[0]
        
    def control_flow_flattening(self, code):
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            print(f"Failed to parse code: {e}")
            return code
        obfuscated_tree = self.ControlFlowFlattener().visit(tree)
        obfuscated_code = astunparse.unparse(obfuscated_tree)
        return obfuscated_code
        

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

    def visit_While(self, node):
        node.test = ast.BoolOp(op=ast.And(), values=[node.test, ast.Name(id=self.opaque_predicate(), ctx=ast.Load())])
        return node

    def visit_Str(self, node):
        encrypted_string = encrypt_with_aes_and_rsa(node.s.encode()).decode()
        index = len(self.encrypted_strings_table)
        self.encrypted_strings_table.append(encrypted_string)
        node.s = f"decrypt_string(encrypted_strings_table[{index}])"
        return node
    
    def obfuscate_string(self, s):
        encrypted_string = encrypt_with_aes_and_rsa(s.encode()).decode()
        index = len(self.encrypted_strings_table)
        self.encrypted_strings_table.append(encrypted_string)
        return f"decrypt_string(encrypted_strings_table[{index}])"

    def obfuscate(self, code):
        code = self.control_flow_flattening(code)
        obfuscated_code = super().obfuscate(code)
        return obfuscated_code

    def parallel_obfuscate(self, code):
        num_processes = multiprocessing.cpu_count()
        pool = multiprocessing.Pool(processes=num_processes)
        chunks = [code[i::num_processes] for i in range(num_processes)]
        results = pool.map(self.obfuscate, chunks)
        obfuscated_code = ''.join(results)
        return obfuscated_code

    def obfuscate_with_opaque_predicates(self, code):
        code = self.control_flow_flattening(code)
        obfuscated_code = super().obfuscate(code)
        opaque_predicates_table_code = "opaque_predicates_table = ["
        for node in self.opaque_predicates_table:
            opaque_predicates_table_code += encrypt_with_aes_and_rsa(ast.dump(node).encode()) + ", "
        opaque_predicates_table_code = opaque_predicates_table_code.rstrip(", ") + "]\n"
        return opaque_predicates_table_code + obfuscated_code

if __name__ == "__main__":
    obfuscator = Supremebfuscator()
    with open('main.py', 'r') as file:
        code = file.read()
    obfuscated_code = obfuscator.obfuscate(code)
    with open('obfuscated_main.py', 'w', encoding='utf-8') as file:
        file.write(obfuscated_code)
