# @Pyfuscator
# @Version: 0.0.9
"""
This obfuscator is protected by the MIT License. Please read the license before using this obfuscator.
This is my custom Python obfuscator. It's not the best, but it's free and open source. I'm not responsible for any damage caused by this program. Use at your own risk.
Created by User319183
"""

# Standard library imports
import ast
import base64
import os
import random
import re
import string
from datetime import datetime
from multiprocessing import Pool, cpu_count



# Local application/library specific imports
import astunparse
from ast import Assign, Call, Load, Name, Str
from modules.console import ConsoleX, LogLevel
from modules.encryption import AdvancedCipher, generate_password

# Setup console
console = ConsoleX()

# Generate a 32-character password
password = generate_password(32)
salt = os.urandom(16)
shift = 3
permutation = {0: 2, 1: 0, 2: 1}

cipher = AdvancedCipher(password, salt, shift, permutation)

# Get current time
now = datetime.now()
current_time = now.strftime("%B %d, %Y at %I:%M:%S %p")
name = "Pyfuscator"
version = "0.0.9"
author = "User319183"
license = "MIT"
description = "Pyfuscator is an advanced Python code obfuscation tool, designed to provide an extra layer of security to your Python code."
contact = "user319183@mailvs.net"

# Define constants
funny_messages = [
    "OBFUSCATED BY PYFUSCATOR",
]

random_variables = [
    "OBFUSCATOR",
]

ascii_loading_screen = """

██████  ██    ██ ███████ ██    ██ ███████  ██████  █████  ████████  ██████  ██████  
██   ██  ██  ██  ██      ██    ██ ██      ██      ██   ██    ██    ██    ██ ██   ██ 
██████    ████   █████   ██    ██ ███████ ██      ███████    ██    ██    ██ ██████  
██         ██    ██      ██    ██      ██ ██      ██   ██    ██    ██    ██ ██   ██ 
██         ██    ██       ██████  ███████  ██████ ██   ██    ██     ██████  ██   ██ 
                                                                                    
                                                                                    
"""


def random_string(min_length=500, max_length=1000):
    """Generates a random string of a random length within the specified range."""
    while True:
        try:
            # Include ASCII characters
            char_sets = string.ascii_letters

            # Add characters from specific Unicode ranges for Chinese
            unicode_ranges = [
                (0x4E00, 0x62FF), (0x6300, 0x77FF), (0x7800, 0x8CFF), (0x8D00, 0x9FCC), (0x3400, 0x4DB5), # Chinese
                (0x0300, 0x0370),  # Combining Diacritical Marks
            ]
            # for start, end in unicode_ranges:
            #     char_sets += "".join(chr(i) for i in range(start, end))
            
            unknown_chars = (
                "吧哈喂嗨こんにちは안녕하세요مرحباПриветΓειασας你好आपकसवगतहこんにちは안녕하세요مرحباПриветΓειασας你好"
                "áéíóúñüÁÉÍÓÚÑÜ"  # Spanish characters
                "àâçéèêëîïôùûüÿÀÂÇÉÈÊËÎÏÔÙÛÜŸ"  # French characters
                "αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"  # Greek characters
                "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"  # Russian characters
                "ÄäÖöÜüß"  # German characters
            )
            char_sets += unknown_chars
            
            # determine the length of the string
            length = random.randint(min_length, max_length)
            
            # generate the string
            console.log(f"Generating random string of length {length}...", LogLevel.INFO)
            return "".join(random.choice(char_sets) for _ in range(length))
        except Exception as e:
            console.log(f"Error during random string generation: {e}", LogLevel.ERROR)




def encrypt_string(self, plaintext):
    return self.cipher.encrypt(plaintext)

class Obfuscator(ast.NodeTransformer):
    def __init__(self, key=None):
        self.names_map = {}
        self.strings_table = []
        self.char_map = {char: i for i, char in enumerate(string.printable)}
        self.parent = None
        self.used_names = set()
       # self.class_names = set() | SOON

    def visit(self, node):
        old_parent = self.parent
        self.parent = node
        try:
            result = super().visit(node)
        except Exception as e:
            console.log(f"Error during node visit: {e}", LogLevel.ERROR)
            return node
        self.parent = old_parent
        return result

    def obfuscate(self, code):
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            console.log(f"Failed to parse code: {e}", LogLevel.ERROR)
            return code
        try:
            obfuscated_tree = self.visit(tree)
            obfuscated_code = astunparse.unparse(obfuscated_tree)
            obfuscated_code = re.sub(
                r"^\s*\n", "", obfuscated_code, flags=re.MULTILINE
            ) # Remove empty lines
            char_map_code = f"char_map = {self.char_map}\n"
            strings_table_code = f"strings_table = {self.strings_table}\n"
            version_info = f"""
# ----------------------------------------
# @{name}
# @Version: {version}
# @Date: {current_time}
# @Author: {author}
# @License: {license}
# @Description: {description}
# @Contact: {contact}
# ----------------------------------------

"""
            lines = obfuscated_code.split("\n")
            for i, message in enumerate(funny_messages):
                random_index = random.randint(0, len(lines))
               # Insert a funny message at a random line. The funny message is a comment but we will work on making it a valid statement later.
                lines.insert(
                    random_index, f'# {random.choice(random_variables)} = "{message}"'
                )
            obfuscated_code = "\n".join(lines)

            return version_info + char_map_code + strings_table_code + obfuscated_code
        except Exception as e:
            console.log(f"Error during obfuscation: {e}", LogLevel.ERROR)
            return code
        
    def visit_Name(self, node):
        """Updates identifiers in names."""
        try:
            if isinstance(node.ctx, (ast.Load, ast.Store)):
                if node.id not in self.names_map and node.id != "__name__":
                    new_name = self.generate_unique_name()
                    self.names_map[node.id] = new_name
                node.id = self.names_map.get(node.id, node.id)
        except Exception as e:
            console.log(f"Error during name visit: {e}", LogLevel.ERROR)
        return node

    def visit_FunctionDef(self, node):
        """Updates identifiers in function definitions."""
        try:
            obfuscated_name = random_string()
            self.names_map[node.name] = obfuscated_name
            node.name = obfuscated_name
        except Exception as e:
            console.log(f"Error during function definition visit: {e}", LogLevel.ERROR)
        return self.generic_visit(node)

    def generate_unique_name(self):
        """Generates a unique name."""
        try:
            while True:
                name = random_string()
                if name not in self.used_names:
                    self.used_names.add(name)
                    return name
        except Exception as e:
           console.log(f"Error during unique name generation: {e}", LogLevel.ERROR)

    def visit_Str(self, node):
        """Encrypts string literals."""
        try:
            encrypted_string = encrypt_string(node.s)
            index = len(self.strings_table)
            self.strings_table.append(encrypted_string)
            node.s = f"decrypt_string(strings_table[{index}])"
        except Exception as e:
            console.log(f"Error during string visit: {e}", LogLevel.ERROR)
        return node

    def visit_Constant(self, node):
        """Obfuscates integer and float literals."""
        try:
            if isinstance(node.value, (int, float)):
                offset = random.randint(1, 99999)
                node.value = node.value + offset - offset
        except Exception as e:
            console.log(f"Error during constant visit: {e}", LogLevel.ERROR)
        return node

    def visit_JoinedStr(self, node):
        """Updates identifiers in joined strings."""
        try:
            for value in node.values:
                if isinstance(value, ast.FormattedValue) and isinstance(
                    value.value, ast.Name
                ):
                    if value.value.id in self.names_map:
                        value.value.id = self.names_map[value.value.id]
        except Exception as e:
            console.log(f"Error during joined string visit: {e}", LogLevel.ERROR)
        return node

    def visit_Call(self, node):
        """Updates identifiers in function calls."""
        try:
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
        except Exception as e:
            console.log(f"Error during call visit: {e}", LogLevel.ERROR)
        return node
    
    def visit_Import(self, node):
        try:
            for alias in node.names:
                if alias.name in self.names_map:
                    alias.name = self.names_map[alias.name]

               # Create a new Call node for the __import__ function
                call_node = Call(
                    func=Name(id='__import__', ctx=Load()),
                    args=[ast.Constant(value=alias.name)],
                    keywords=[]
                )
                assign_node = Assign(
                    targets=[Name(id=alias.name, ctx=Load())],
                    value=call_node
                )
                return assign_node

        except Exception as e:
            console.log(f"Error during import visit: {e}", LogLevel.ERROR)
        return node

    def visit_ImportFrom(self, node):
        try:
            if node.module in self.names_map:
                node.module = self.names_map[node.module]
            for alias in node.names:
                if alias.name in self.names_map:
                    alias.name = self.names_map[alias.name]
            
           # Create a new Call node for the __import__ function
            call_node = Call(
                func=Name(id='__import__', ctx=Load()),
                args=[Str(s=node.module)],
                keywords=[]
            )
            assign_node = Assign(
                targets=[Name(id=node.module, ctx=Load())],
                value=call_node
            )
            return assign_node

        except Exception as e:
            console.log(f"Error during import from visit: {e}", LogLevel.ERROR)
        return node
    
class AdvancedObfuscator(Obfuscator):
    def __init__(self):
        super().__init__()
        self.anti_debugger_code_inserted = False
        self.anti_vm_code_inserted = False

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
        """Shuffles the order of the statements in a node."""
        try:
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
        except Exception as e:
            console.log(f"Error during code flattening: {e}", LogLevel.ERROR)
        return node

    def flatten_if(self, if_node, control_var, range):
        """Flattens if statements."""
        try:
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
        except Exception as e:
            console.log(f"Error during if flattening: {e}", LogLevel.ERROR)
        return if_node

    def proprietary_logic(self, node):
        """Encrypts string literals and function names."""
        try:
            if isinstance(node, ast.Str):
                encrypted_string = encrypt_string(node.s)
                return ast.Str(s=encrypted_string)
            else:
                encrypted_name = encrypt_string(node.name)
                print_node = ast.Expr(
                    value=ast.Call(
                        func=ast.Name(id="print", ctx=ast.Load()),
                        args=[ast.Str(s=encrypted_name)],
                        keywords=[],
                    )
                )
                node.body.insert(0, print_node)
        except Exception as e:
            console.log(f"Error during proprietary logic application: {e}", LogLevel.ERROR)
        return node

    def safeguard(self, node):
        """Replaces integer literals with expressions that evaluate to the same integer."""
        try:
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
        except Exception as e:
            console.log(f"Error during safeguard application: {e}", LogLevel.ERROR)
        return node

    def generate_dead_code(self):
        """Generates a piece of "dead code"."""
        try:
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
        except Exception as e:
            console.log(f"Error during dead code generation: {e}", LogLevel.ERROR)
            
    def visit_FunctionDef(self, node):
        """Obfuscates a function definition."""
        try:
            console.print(f"Obfuscating function: {node.name}", LogLevel.INFO)

            obfuscated_name = random_string()
            self.names_map[node.name] = obfuscated_name
            node.name = obfuscated_name

            node = self.flatten(node)
            node = self.proprietary_logic(node)
            node = self.safeguard(node)
            dead_code = self.generate_dead_code()
            node.body.insert(random.randint(0, len(node.body)), dead_code)
            console.log(f"Finished obfuscating function: {node.name}", LogLevel.SUCCESS)
        except Exception as e:
            console.log(f"Error during function obfuscation: {e}", LogLevel.ERROR)
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
debugger_detected = base64.b64decode(b'RGVidWdnaW5nIHRvb2wgZGV0ZWN0ZWQuIFByb2dyYW0gd2lsbCB0ZXJtaW5hdGUu').decode() # "Debugging tool detected. Program will terminate."
pyfuscator = base64.b64decode(b'UHlmdXNjYXRvciAtIEFudGktRGVidWdnZXI=').decode() # "Pyfuscator - Anti-Debugger"

# Encoded function names
message_box = getattr(ctypes.windll.user32, base64.b64decode(b'TWVzc2FnZUJveFc=').decode())
exit_func = getattr(os, base64.b64decode(b'X2V4aXQ=').decode())
is_debugger_present = getattr(ctypes.windll.kernel32, base64.b64decode(b'SXNEZWJ1Z2dlclByZXNlbnQ=').decode())

# Check if a debugger is attached
if getattr(sys, base64.b64decode(b'Z2V0dHJhY2U=').decode())() is not None:
    message_box(0, debugger_detected, pyfuscator, 1)
    exit_func(1)
    
# Check for the presence of a debugger using the IsDebuggerPresent Windows API function
if is_debugger_present():
    message_box(0, debugger_detected, pyfuscator, 1)
    exit_func(1)

# Encoded debugger-related processes names
debugger_processes = [base64.b64decode(b'Z2Ri').decode(), # gdb
base64.b64decode(b'bGxkYg==').decode(), # lldb
base64.b64decode(b'd2luZGJn').decode(), # windbg
base64.b64decode(b'aWRhcQ==').decode(), # idaq
base64.b64decode(b'aWRhcTY0').decode(), # idaq64
base64.b64decode(b'eDY0X2RiZw==').decode(), # x64_dbg
base64.b64decode(b'b2xseWRiZw==').decode(), # ollydbg
base64.b64decode(b'aW1tdW5pdHlkZWJ1Z2dlcg==').decode(), # immunitydebugger 
base64.b64decode(b'ZWNsaXBzZQ==').decode(), # eclipse
base64.b64decode(b'cHlyYWhybQ==').decode(), # pycharm
base64.b64decode(b'bmV0YmVhbnM=').decode(), # netbeans
base64.b64decode(b'Y29kZWJsb2Nrcw==').decode(), # codeblocks
base64.b64decode(b'dmlzdWFsbHN0dWRpbyE=').decode(), # visualstudio
base64.b64decode(b'cmFkYXJlMg==').decode()] # radare2

running_processes = [proc.info['name'] for proc in psutil.process_iter(attrs=['name'])]
for debugger in debugger_processes:
    if debugger in running_processes:
        message_box(0, debugger_detected, pyfuscator, 1)
        exit_func(1)

# Timing check
start_time = time.time()
time.sleep(0.001) # Reduced sleep time to 0.001 seconds
end_time = time.time()
if end_time - start_time > 0.005:
    message_box(0, debugger_detected, pyfuscator, 1)
    exit_func(1)
"""
        return ast.parse(anti_debugger_code)
    
    def generate_anti_vm_code(self):
        anti_vm_code = """
import os
import ctypes
import base64

# Encoded strings
vm_detected = base64.b64decode(b'VmlydHVhbCBNYWNoaW5lIGRldGVjdGVkLiBQcm9ncmFtIHdpbGwgdGVybWluYXRlLg==').decode() # "Virtual Machine detected. Program will terminate."
pyfuscator = base64.b64decode(b'UHlmdXNjYXRvciAtIEFudGktVk0=').decode() # "Pyfuscator - Anti-VM"

# Encoded function names
message_box = getattr(ctypes.windll.user32, base64.b64decode(b'TWVzc2FnZUJveFc=').decode())
exit_func = getattr(os, base64.b64decode(b'X2V4aXQ=').decode())

# Encoded VM-related artifacts
vm_artifacts = [
    base64.b64decode(b'Vk13YXJlIFdvcmtzdGF0aW9uIFBsYXllcg==').decode(), # VMware Workstation Player
    base64.b64decode(b'VmlydHVhbEJveA==').decode(), # VirtualBox
    base64.b64decode(b'SHlwZXItVg==').decode(), # Hyper-V
    base64.b64decode(b'UGFyYWxsZWxzIERlc2t0b3A=').decode(), # Parallels Desktop
    base64.b64decode(b'Vk13YXJlIFdvcmtzdGF0aW9uIFBybw==').decode(), # VMware Workstation Pro
    base64.b64decode(b'Vk13YXJlIEZ1c2lvbg==').decode(), # VMware Fusion
    base64.b64decode(b'UVVFTQ==').decode(), # QEMU
    base64.b64decode(b'S1ZN').decode(), # KVM
    base64.b64decode(b'WGVu').decode(), # Xen
    base64.b64decode(b'UmVkIEhhdCBWaXJ0dWFsaXphdGlvbg==').decode(), # Red Hat Virtualization
]
                

# Check for VM artifacts in system information
system_info = os.popen('systeminfo').read().lower()
for artifact in vm_artifacts:
    if artifact in system_info:
        message_box(0, vm_detected, pyfuscator, 1)
        exit_func(1)
        
"""
        return ast.parse(anti_vm_code)

    def visit_Module(self, node):
        """Inserts anti-debugger code, anti-VM code and dead code snippets into the module."""
        try:
            if not self.anti_debugger_code_inserted:
                node.body.insert(
                    random.randint(0, len(node.body)), self.generate_anti_debugger_code()
                )
                self.anti_debugger_code_inserted = True

            if not self.anti_vm_code_inserted:
                node.body.insert(
                    random.randint(0, len(node.body)), self.generate_anti_vm_code()
                )
                self.anti_vm_code_inserted = True

            for _ in range(random.randint(1, 100)):
                node.body.insert(
                    random.randint(0, len(node.body)), self.generate_dead_code()
                )
            self.generic_visit(node)
        except Exception as e:
            console.log(f"Error during module visit: {e}", LogLevel.ERROR)
        return node

    def visit_While(self, node):
        """Replaces while loops with for loops."""
        try:
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
        except Exception as e:
            console.log(f"Error during while loop visit: {e}", LogLevel.ERROR)
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

        # Define the control variable
        assign_node = ast.Assign(
            targets=[ast.Name(id=control_var, ctx=ast.Store())],
            value=ast.Constant(value=0),
            type_comment=None,
        )

        # Create a list of the bodies of the if and else branches
        bodies = [node.body]
        if node.orelse:
            bodies.append(node.orelse)

        # Insert the assign node at the start of each body
        for body in bodies:
            body.insert(0, assign_node)

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
        x = random.randint(1, 10000)
        condition = ast.Compare(
            left=ast.BinOp(
                left=ast.BinOp(
                    left=ast.Constant(value=x),
                    op=ast.Mult(),
                    right=ast.Constant(value=x),
                ),
                op=ast.Sub(),
                right=ast.Constant(value=x),
            ),
            ops=[ast.Mod()],
            comparators=[ast.Constant(value=2)],
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
        encrypted_string = encrypt_string(node.s.encode()).decode()
        index = len(self.encrypted_strings_table)
        self.encrypted_strings_table.append(encrypted_string)
        node.s = f"decrypt_string(encrypted_strings_table[{index}])"
        return node

    def obfuscate_string(self, s):
        encrypted_string = encrypt_string(s.encode()).decode()
        index = len(self.encrypted_strings_table)
        self.encrypted_strings_table.append(encrypted_string)
        return f"decrypt_string(encrypted_strings_table[{index}])"

    def obfuscate(self, code):
        # code = self.control_flow_flattening(code)
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
        try:
            obfuscator = Supremebfuscator()
            obfuscated_block = obfuscator.obfuscate(block)
            console.log(f"Successfully obfuscated block", LogLevel.SUCCESS)
            return obfuscated_block
        except Exception as e:
            console.log(f"Error during block obfuscation: {e}", LogLevel.ERROR)
            return block # Return the original block if obfuscation fails


    def obfuscate_with_opaque_predicates(self, code):
        code = self.control_flow_flattening(code)
        obfuscated_code = super().obfuscate(code)
        opaque_predicates_table_code = "opaque_predicates_table = ["
        for node in self.opaque_predicates_table:
            opaque_predicates_table_code += (
                encrypt_string(ast.dump(node).encode()) + ", "
            )
        opaque_predicates_table_code = opaque_predicates_table_code.rstrip(", ") + "]\n"
        return opaque_predicates_table_code + obfuscated_code

def get_input_file():
    input_file = console.input("Enter the name of the file to obfuscate: ", fg="pink")
    if not input_file or not os.path.exists(input_file):
        console.log("Invalid file name or file does not exist", LogLevel.ERROR)
        return None
    return input_file

def get_output_file():
    output_file = console.input("Enter the name of the output file: ", fg="pink")
    if not output_file:
        console.log("Invalid file name", LogLevel.ERROR)
        return None
    return output_file

def obfuscate_file(input_file, output_file):
    console.log(f"Reading from file: {input_file}", LogLevel.INFO)
    with open(input_file, "r", encoding="utf-8") as file:
        code = file.read()

    console.log("Starting obfuscation", LogLevel.INFO)
    obfuscator = Supremebfuscator()
    obfuscated_code = obfuscator.obfuscate(code)
    console.log("Finished obfuscation", LogLevel.SUCCESS)

    console.log(f"Writing to file: {output_file}", LogLevel.INFO)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(obfuscated_code)

    console.log(f"Obfuscated code saved to {output_file}", LogLevel.SUCCESS)

def main():
    console.clear()
    console.print(ascii_loading_screen, fg="pink")
    console.title("Pyfuscator")

    input_file = get_input_file()
    if not input_file:
        return

    output_file = get_output_file()
    if not output_file:
        return

    obfuscate_file(input_file, output_file)

    console.input("Press any key to exit...", fg="pink")

if __name__ == "__main__":
    main()