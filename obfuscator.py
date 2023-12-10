# py obfuscator.py

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
from multiprocessing import Pool, cpu_count
import re
import os
import ctypes

# Setup console
from modules.console import ConsoleX, LogLevel

console = ConsoleX()

# SOON
with open("config.json") as f:
    config = json.load(f)

KEY = get_random_bytes(32)
RSA_KEY = RSA.generate(2048)
RSA_CIPHER = PKCS1_OAEP.new(RSA_KEY)

funny_messages = [
    "User319183 was here!",
    "This code was obfuscated by Pyfuscator",
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

ascii_loading_screen = """

██████  ██    ██ ███████ ██    ██ ███████  ██████  █████  ████████  ██████  ██████  
██   ██  ██  ██  ██      ██    ██ ██      ██      ██   ██    ██    ██    ██ ██   ██ 
██████    ████   █████   ██    ██ ███████ ██      ███████    ██    ██    ██ ██████  
██         ██    ██      ██    ██      ██ ██      ██   ██    ██    ██    ██ ██   ██ 
██         ██    ██       ██████  ███████  ██████ ██   ██    ██     ██████  ██   ██ 
                                                                                    
                                                                                    
"""


def random_string(length=500):
    ascii_and_digits = string.ascii_letters
    spanish_chars = "áéíóúñüÁÉÍÓÚÑÜ"
    french_chars = "àâæçéèêëîïôœùûüÿÀÂÆÇÉÈÊËÎÏÔŒÙÛÜŸ"
    chinese_chars = "丨丿乙亅人亻仌仨仡仫伋伢佤佥侑侔俉俣俨俪俳倌倬倻偀偁偂偃偕偰偱偲側偵偸偺偽傀傃傈傔傕傖傘備傛傜傞傠傡傢傪傫傭傯傰傱傳傴債傶傷傸傹傼傽傾僀僂僄僅僇僉僊僎僐僑僒僓僔僕僖僗僘僙僚僛僜僝僞僟僠僡僢僣僤僥僨僩僪僫僬僭僮僯僰僱僲僴僶僷僸價僺僻僼僽僾僿儀儁儂儃億儅儈儉儊儌儍儎儏儐儑儒儓儔儕儖儗儘儙儚儛儜儝儞償儠儡儢儣儤儥儦儧儨儩優儫儬儭儮儯儰儱儲儳儴儵儶儷儸儹儺儻儼儽儾儿兀兂兊兌兎兏児兒兓兗兘兙兛兝兞兟兠兡兣兤兦內兩"
    unknown_chars = (
        "吧哈喂嗨こんにちは안녕하세요مرحباПриветΓειασας你好आपकसवगतहこんにちは안녕하세요مرحباПриветΓειασας你好"
    )
    return "".join(
        random.choices(
            ascii_and_digits
            + spanish_chars
            + french_chars
            + chinese_chars
            + unknown_chars,
            k=length,
        )
    )


def encrypt_with_aes_and_rsa(plain_text):
    IV = get_random_bytes(16)
    cipher_aes = AES.new(KEY, AES.MODE_CFB, IV)
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
        self.used_names = set()  # Used to prevent name collisions

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
            console.log(f"Failed to parse code: {e}", LogLevel.ERROR)
            return code
        obfuscated_tree = self.visit(tree)
        obfuscated_code = astunparse.unparse(obfuscated_tree)
        obfuscated_code = re.sub(
            r"^\s*\n", "", obfuscated_code, flags=re.MULTILINE
        )  # Remove empty lines
        char_map_code = f"char_map = {self.char_map}\n"
        strings_table_code = f"strings_table = {self.strings_table}\n"
        info = {
            "Pyfuscator": {
                "Credits": {
                    "User319183": "Free | Open Source | MIT License",
                },
                "features": {
                    "random_string_generation": "✅",
                    "aes_and_rsa_encryption": "✅",
                    "string_encryption": "✅",
                    "string_decryption": "✅",
                    "code_obfuscation": "✅",
                    "name_obfuscation": "✅",
                    "function_name_obfuscation": "✅",
                    "string_obfuscation": "✅",
                    "constant_obfuscation": "✅",
                    "call_obfuscation": "✅",
                    "Advanced_Obfuscation": {
                        "code_flattening": "✅",
                        "proprietary_logic_insertion": "✅",
                        "safeguard_insertion": "✅",
                        "dead_code_insertion": "✅",
                        "code_substitution": "✅",
                        "dummy_code_insertion": "✅",
                        "variable_renaming": "✅",
                        "advanced_anti_debugger": {
                            "debugger_attachment_detection": "✅",
                            "debugger_process_detection": "✅",
                            "timing_check": "✅",
                            "code_obfuscation": "✅",
                            "debugger_evasion_techniques": "✅",
                            "stealth_techniques": "✅",
                            "environment_checks": "✅",
                            "anti_memory_dumping": "✅",
                            "anti_tampering": "⏳",
                            "anti_virtual_machine": "⏳",
                        },
                    },
                    "SupremeObfuscation": {
                        "opaque_predicates": "✅",
                        "encrypted_strings": "✅",
                        "control_flow_flattening": "✅",
                        "parallel_obfuscation": "✅",
                    },
                },
            }
        }

        version_info = (
            "credits = " + json.dumps(info, indent=4, ensure_ascii=False) + "\n"
        )
        lines = obfuscated_code.split("\n")
        for i, message in enumerate(funny_messages):
            random_index = random.randint(0, len(lines))
            # Insert a funny message at a random line. The funny message is a comment but we will work on making it a valid statement later.
            lines.insert(
                random_index, f'# {random.choice(random_variables)} = "{message}"'
            )
        obfuscated_code = "\n".join(lines)

        return version_info + char_map_code + strings_table_code + obfuscated_code

    def visit_Name(self, node):
        if isinstance(node.ctx, (ast.Load, ast.Store)):
            if node.id not in self.names_map:
                new_name = self.generate_unique_name()
                self.names_map[node.id] = new_name
            node.id = self.names_map.get(node.id, node.id)
        return node

    def visit_FunctionDef(self, node):
        obfuscated_name = "".join(random.choices(string.ascii_letters, k=10))
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
        node.s = f"decrypt_string(strings_table[{index}])"  # Decrypt the string before returning it
        return node

    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)):
            offset = random.randint(1, 99999)
            node.value = (
                node.value + offset - offset
            )  # Obfuscate the number by adding and subtracting the offset
        return node

    def visit_JoinedStr(self, node):
        for value in node.values:
            if isinstance(value, ast.FormattedValue) and isinstance(
                value.value, ast.Name
            ):
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
                    if isinstance(value, ast.FormattedValue) and isinstance(
                        value.value, ast.Name
                    ):
                        if value.value.id in self.names_map:
                            value.value.id = self.names_map[value.value.id]
        return node


class AdvancedObfuscator(Obfuscator):
    def __init__(self):
        super().__init__()
        self.anti_debugger_code_inserted = False

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
        ranges_table = [[i, i + 1] for i in range(len(node.body))]

        for i, body_node in enumerate(shuffled_body):
            if isinstance(body_node, ast.If):
                # Handle if statement
                body_node = self.flatten_if(body_node, control_var, ranges_table[i])
            else:
                # Handle other statements
                if_node = ast.If(
                    test=ast.Compare(
                        left=ast.Name(id=control_var, ctx=ast.Load()),
                        ops=[ast.GtE(), ast.Lt()],
                        comparators=[
                            ast.Constant(value=ranges_table[i][0]),
                            ast.Constant(value=ranges_table[i][1]),
                        ],
                    ),
                    body=[
                        body_node,
                        ast.Assign(
                            targets=[ast.Name(id=control_var, ctx=ast.Store())],
                            value=ast.BinOp(
                                left=ast.Name(id=control_var, ctx=ast.Load()),
                                op=ast.Add(),
                                right=ast.Constant(value=1),
                            ),
                        ),
                    ],
                    orelse=[],
                )
                shuffled_body[i] = if_node

        node.body = [
            ast.Assign(
                targets=[ast.Name(id=control_var, ctx=ast.Store())],
                value=ast.Constant(value=0),
            ),
            ast.While(test=ast.Constant(value=True), body=shuffled_body, orelse=[]),
        ]

        return node

    def flatten_if(self, if_node, control_var, range):
        # Flatten the test, body, and orelse parts of the if statement
        if_node.test = self.flatten(if_node.test)
        if_node.body = self.flatten(if_node.body)
        if_node.orelse = self.flatten(if_node.orelse)

        # Add control variable and if statement to control execution order
        if_control_var = random_string()
        if_node.body.insert(
            0,
            ast.Assign(
                targets=[ast.Name(id=if_control_var, ctx=ast.Store())],
                value=ast.Constant(value=0),
            ),
        )
        if_node.body.append(
            ast.If(
                test=ast.Compare(
                    left=ast.Name(id=if_control_var, ctx=ast.Load()),
                    ops=[ast.GtE(), ast.Lt()],
                    comparators=[
                        ast.Constant(value=range[0]),
                        ast.Constant(value=range[1]),
                    ],
                ),
                body=[
                    ast.Assign(
                        targets=[ast.Name(id=control_var, ctx=ast.Store())],
                        value=ast.BinOp(
                            left=ast.Name(id=control_var, ctx=ast.Load()),
                            op=ast.Add(),
                            right=ast.Constant(value=1),
                        ),
                    )
                ],
                orelse=[],
            )
        )

        # Add control variable and if statement to control execution order of orelse part
        else_control_var = random_string()
        if_node.orelse.insert(
            0,
            ast.Assign(
                targets=[ast.Name(id=else_control_var, ctx=ast.Store())],
                value=ast.Constant(value=0),
            ),
        )
        if_node.orelse.append(
            ast.If(
                test=ast.Compare(
                    left=ast.Name(id=else_control_var, ctx=ast.Load()),
                    ops=[ast.GtE(), ast.Lt()],
                    comparators=[
                        ast.Constant(value=range[0]),
                        ast.Constant(value=range[1]),
                    ],
                ),
                body=[
                    ast.Assign(
                        targets=[ast.Name(id=control_var, ctx=ast.Store())],
                        value=ast.BinOp(
                            left=ast.Name(id=control_var, ctx=ast.Load()),
                            op=ast.Add(),
                            right=ast.Constant(value=1),
                        ),
                    )
                ],
                orelse=[],
            )
        )

        return if_node

    def proprietary_logic(self, node):
        if isinstance(node, ast.Str):
            encrypted_string = encrypt_with_aes_and_rsa(node.s)
            return ast.Str(s=encrypted_string)
        else:
            encrypted_name = encrypt_with_aes_and_rsa(node.name)
            print_node = ast.Expr(
                value=ast.Call(
                    func=ast.Name(id="print", ctx=ast.Load()),
                    args=[ast.Str(s=encrypted_name)],
                    keywords=[],
                )
            )
            node.body.insert(0, print_node)
            return node

    def safeguard(self, node):
        class ReplaceIntegers(ast.NodeTransformer):
            def visit_Constant(self, node):
                if isinstance(node.value, int):
                    return ast.BinOp(
                        left=ast.Constant(value=node.value + 1),
                        op=ast.Sub(),
                        right=ast.Constant(value=1),
                    )
                return node

        ReplaceIntegers().visit(node)
        return node

    def generate_dead_code(self):
        dead_code_type = random.choice(["noop_loop", "meaningless_calc", "unused_var"])
        if dead_code_type == "noop_loop":
            return ast.For(
                target=ast.Name(id="_", ctx=ast.Store()),
                iter=ast.Call(
                    func=ast.Name(id="range", ctx=ast.Load()),
                    args=[ast.Constant(value=random.randint(1, 10000))],
                    keywords=[],
                ),
                body=[ast.Pass()],
                orelse=[],
            )
        elif dead_code_type == "meaningless_calc":
            return ast.Expr(
                value=ast.BinOp(
                    left=ast.Constant(value=random.randint(1, 99999)),
                    op=ast.Add(),
                    right=ast.Constant(value=random.randint(1, 99999)),
                )
            )
        elif dead_code_type == "unused_var":
            return ast.Assign(
                targets=[ast.Name(id=random_string(), ctx=ast.Store())],
                value=ast.Constant(value=random.randint(1, 99999)),
            )

    def visit_FunctionDef(self, node):
        console.log(f"Obfuscating function: {node.name}", LogLevel.INFO)
        node = self.flatten(node)
        node = self.proprietary_logic(node)
        node = self.safeguard(node)
        dead_code = self.generate_dead_code()
        node.body.insert(random.randint(0, len(node.body)), dead_code)
        console.log(f"Finished obfuscating function: {node.name}", LogLevel.SUCCESS)
        return super().visit_FunctionDef(node)

    def generate_anti_debugger_code(self):
        anti_debugger_code = """
import base64
import ctypes
import os
import sys
import time
import psutil

# Encoded strings
debugger_detected = base64.b64decode('RGVidWdnaW5nIHRvb2wgZGV0ZWN0ZWQuIFByb2dyYW0gd2lsbCB0ZXJtaW5hdGUu').decode()  # "Debugging tool detected. Program will terminate."
pyfuscator = base64.b64decode('UHlmdXNjYXRvciAtIEFudGktRGVidWdnZXI=').decode()  # "Pyfuscator - Anti-Debugger"

# Encoded function names
message_box = getattr(ctypes.windll.user32, base64.b64decode('TWVzc2FnZUJveFc=').decode())
exit_func = getattr(os, base64.b64decode('X2V4aXQ=').decode())

# Check if a debugger is attached
if getattr(sys, base64.b64decode('Z2V0dHJhY2U=').decode())() is not None:
    message_box(0, debugger_detected, pyfuscator, 1)
    exit_func(1)

# Check for debugger-related processes
debugger_processes = ['gdb', 'lldb', 'windbg', 'idaq', 'idaq64', 'x64_dbg', 'ollydbg', 'immunitydebugger', 'eclipse', 'pycharm', 'netbeans', 'codeblocks', 'visualstudio', 'radare2', 'jdb']
running_processes = [proc.info['name'] for proc in psutil.process_iter(attrs=['name'])]
for debugger in debugger_processes:
    if debugger in running_processes:
        message_box(0, debugger_detected, pyfuscator, 1)
        exit_func(1)
        
# Check if pdb is in sys.modules (soon)

# Timing check
start_time = time.time()
time.sleep(0.001)  # Reduced sleep time to 0.001 seconds
end_time = time.time()
if end_time - start_time > 0.005:  # Increased threshold to 0.005
    message_box(0, debugger_detected, pyfuscator, 1)
    exit_func(1)
"""
        return ast.parse(anti_debugger_code)

    def visit_Module(self, node):
        if not self.anti_debugger_code_inserted:
            node.body.insert(
                random.randint(0, len(node.body)), self.generate_anti_debugger_code()
            )
            self.anti_debugger_code_inserted = True
        for _ in range(random.randint(1, 100)):
            node.body.insert(
                random.randint(0, len(node.body)), self.generate_dead_code()
            )
        self.generic_visit(node)
        return node

    def visit_While(self, node):
        new_node = ast.For(
            target=ast.Name(id="_", ctx=ast.Store()),
            iter=ast.Call(
                func=ast.Name(id="range", ctx=ast.Load()),
                args=[ast.Constant(value=1000000)],
                keywords=[],
            ),
            body=node.body,
            orelse=[],
        )
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
                    if_elif_statements.append(
                        ast.If(
                            test=ast.Compare(
                                left=ast.Name(id=control_var, ctx=ast.Load()),
                                ops=[ast.Eq()],
                                comparators=[ast.Constant(value=index)],
                            ),
                            body=body,
                            orelse=[],
                        )
                    )
                else:
                    if_elif_statements[-1].orelse.append(
                        ast.If(
                            test=ast.Compare(
                                left=ast.Name(id=control_var, ctx=ast.Load()),
                                ops=[ast.Eq()],
                                comparators=[ast.Constant(value=index)],
                            ),
                            body=body,
                            orelse=[],
                        )
                    )

            return if_elif_statements[0]

    def control_flow_flattening(self, code):
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            console.log(f"Failed to parse code: {e}", LogLevel.ERROR)
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
                right=ast.Constant(value=random.randint(1, 10000)),
            ),
            ops=[ast.Eq()],
            comparators=[
                ast.BinOp(
                    left=ast.Constant(value=random.randint(1, 10000)),
                    op=ast.Add(),
                    right=ast.Constant(value=random.randint(1, 10000)),
                )
            ],
        )
        self.opaque_predicates_table.append(condition)
        return f"opaque_predicates_table[{len(self.opaque_predicates_table) - 1}]"

    def visit_While(self, node):
        node.test = ast.BoolOp(
            op=ast.And(),
            values=[node.test, ast.Name(id=self.opaque_predicate(), ctx=ast.Load())],
        )
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
        blocks = self.split_into_blocks(code)

        with Pool(cpu_count()) as p:
            obfuscated_blocks = p.map(self.obfuscate_block, blocks)

        obfuscated_code = "".join(obfuscated_blocks)

        return obfuscated_code

    def split_into_blocks(self, code):
        module = ast.parse(code)

        blocks = []
        for node in module.body:
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                block = ast.unparse(node)
                blocks.append(block)

        return blocks

    def obfuscate_block(self, block):
        obfuscator = Obfuscator()

        obfuscated_block = obfuscator.obfuscate(block)

        return obfuscated_block

    def obfuscate_with_opaque_predicates(self, code):
        code = self.control_flow_flattening(code)
        obfuscated_code = super().obfuscate(code)
        opaque_predicates_table_code = "opaque_predicates_table = ["
        for node in self.opaque_predicates_table:
            opaque_predicates_table_code += (
                encrypt_with_aes_and_rsa(ast.dump(node).encode()) + ", "
            )
        opaque_predicates_table_code = opaque_predicates_table_code.rstrip(", ") + "]\n"
        return opaque_predicates_table_code + obfuscated_code


def main():
    # Anti-memory dumping code
    PROCESS_ALL_ACCESS = 0x1F0FFF
    PAGE_NOACCESS = 0x01

    hProcess = ctypes.windll.kernel32.OpenProcess(
        PROCESS_ALL_ACCESS, False, os.getpid()
    )
    base_address = ctypes.windll.kernel32.GetModuleHandleW(None)

    old_protect = ctypes.c_ulong(0)
    ctypes.windll.kernel32.VirtualProtectEx(
        hProcess, base_address, 1, PAGE_NOACCESS, ctypes.byref(old_protect)
    )

    console.clear()
    console.print(ascii_loading_screen, fg="pink")
    console.title("Pyfuscator")

    input_file = console.input("Enter the name of the file to obfuscate: ", fg="pink")
    # input_file = "main.py"
    console.log(f"Reading from file: {input_file}", LogLevel.INFO)
    with open(input_file, "r", encoding="utf-8") as file:
        code = file.read()

    console.log("Starting obfuscation", LogLevel.INFO)
    obfuscator = AdvancedObfuscator()
    obfuscated_code = obfuscator.obfuscate(code)
    console.log("Finished obfuscation", LogLevel.SUCCESS)

    # output_file = "obfuscated_main.py"
    output_file = console.input("Enter the name of the output file: ", fg="pink")
    console.log(f"Writing to file: {output_file}", LogLevel.INFO)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(obfuscated_code)

    console.log(f"Obfuscated code saved to {output_file}", LogLevel.SUCCESS)
    console.input("Press any key to exit...", fg="pink")


if __name__ == "__main__":
    main()
